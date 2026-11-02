import unittest,sys,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from simulation import simulate,DEFAULTS
from app import StandardLibraryApp
from io import BytesIO
import json
class ModelTests(unittest.TestCase):
    def test_deterministic(self): self.assertEqual(simulate(DEFAULTS),simulate(DEFAULTS))
    def test_12_periods(self): self.assertEqual(len(simulate(DEFAULTS)['periods']),12)
    def test_bounds(self):
        for x in (0,100):
            p={'confidence':x,'sell_pressure':x,'bank_capacity':x,'intervention':'early'}
            r=simulate(p)
            self.assertTrue(all(0<=v['stability_index']<=100 and v['bank_remaining']>=0 and v['public_remaining']>=0 for v in r['periods']))
    def test_no_replenishment(self):
        p={'confidence':0,'sell_pressure':100,'bank_capacity':5,'intervention':'early'}
        a=simulate(p)['periods']
        self.assertTrue(all(a[i+1]['bank_remaining']<=a[i]['bank_remaining'] for i in range(11)))
        self.assertTrue(all(a[i+1]['public_remaining']<=a[i]['public_remaining'] for i in range(11)))
        self.assertEqual(a[-1]['bank_remaining'],0)
    def test_intervention(self):
        p={**DEFAULTS,'intervention':'none'}
        none=simulate(p)['summary']['last_stability_index']
        early=simulate({**p,'intervention':'early'})['summary']['last_stability_index']
        self.assertGreaterEqual(early,none)
    def test_sell_pressure(self):
        less=simulate({**DEFAULTS,'sell_pressure':0})['summary']['last_stability_index']
        more=simulate({**DEFAULTS,'sell_pressure':100})['summary']['last_stability_index']
        self.assertGreaterEqual(less,more)
    def test_validation(self):
        for bad in ({**DEFAULTS,'confidence':-1},{**DEFAULTS,'confidence':101},
                    {**DEFAULTS,'confidence':'70'},{**DEFAULTS,'confidence':True},
                    {**DEFAULTS,'intervention':'maybe'},{}):
            with self.assertRaises(ValueError):simulate(bad)
    def test_stdlib_api(self):
        srv=StandardLibraryApp()
        def call(path,method='GET',data=None):
            raw=json.dumps(data or {}).encode(); r=[]
            ret=srv({'PATH_INFO':path,'REQUEST_METHOD':method,'CONTENT_LENGTH':str(len(raw)),'wsgi.input':BytesIO(raw)},lambda s,h:r.append(s))
            return r[0],json.loads(b''.join(ret))
        status,p=call('/api/health');self.assertTrue(status.startswith('200'));self.assertEqual(p['status'],'ok')
        status,p=call('/api/simulate','POST',DEFAULTS);self.assertTrue(status.startswith('200'));self.assertEqual(len(p['periods']),12)
        status,p=call('/api/simulate','POST',{'invalid':1});self.assertTrue(status.startswith('400'))
if __name__=='__main__':unittest.main()
