from pyiso import client_factory
import pandas as pd

nyiso = client_factory('NYISO', timeout_seconds=60)
data = nyiso.get_generation(latest=True)
df = pd.DataFrame(data)
print(df.head(10))