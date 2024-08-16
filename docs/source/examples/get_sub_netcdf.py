# Importa a ferramenta
import subsaz.CPTEC_SUB as SUB

# Inicializa o construtor
sub = SUB.model()

# Data Condição Inicial (IC)
date = '20230104'

# variavel
var = 'prec'

# produto
product = 'week'

# campo
field = 'anomalies'

# passo depende do produto escolhido
step = '01'

# Requisição dos dados
f = sub.load(date=date, var=var, step=step, product=product ,field=field)

# Salvar XArray em NetCDF
f.to_netcdf('sub_202301104.nc')

quit()