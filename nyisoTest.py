from pyiso import client_factory
import pandas as pd

nyiso = client_factory('NYISO', timeout_seconds=120)
# data = nyiso.get_generation(latest=True)
# df = pd.DataFrame(data)
# print(df.head(10))
zonedata=nyiso.get_dam_lbmp(node_id='59TH STREET_GT_1',start_at='20200130',end_at='20200131',category='gen')
gendata=nyiso.get_dam_lbmp(node_id='59TH STREET_GT_1',start_at='20200130',end_at='20200131',category='gen')
df = pd.DataFrame(gendata)
df1=df.query('node_id == "59TH STREET_GT_1"')
print(df1.head(10))
print(len(df1))
