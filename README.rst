[![Logo](https://github.com/framework-CPTEC/_static/blob/main/framework.png)](https://www.cptec.inpe.br/)


### Framework-CPTEC 

É um pacote in Python para a distribuição de dados brutos dos Modelos Numéricos de forma segmentada/particionada. Com esse pacote o usuário não necessita fazer o Download de todo o volume bruto o pacote auxilia a manipular somente a sua necessidade.

support Python >= 3.10.

## Instalação 

- Criar ambiente conda

conda create -n cptec python=3.10

conda activate cptec

- Instalar Pacotes

conda install -c conda-forge matplotlib pycurl cfgrib netCDF4 pynio xarray dask esmpy scipy mpi4py xesmf

- Instalar Pacote

### Via pip

pip install -i https://test.pypi.org/simple/ cptec-model

### Via fonte

git clone https://github.com/framework-CPTEC/CPTEC-user.git  

cd CPTEC-user 

python setup.py install

## Uso

import cptecmodel.CPTEC_BAM as BAM

bam = BAM.model()

date = '2023010800'

vars = ['t', 'u10m']

levels = [1000, 850]

steps = 3

f = bam.load(date=date, var=vars,level=levels, steps=steps)

## Observações

Após a inicialização do Modelo Específico algumas configurações são plotadas. 

Ex.:

The Brazilian Global Atmospheric Model (TQ0666L064 / Hybrid) 

Forecast data available for reading between 20221211 and 20221221.

Surface variables: t2m, u10m, v10m, slp, psfc, precip
                   terrain, sbcape, sbcin, pw.
Level variables:   t, u, v, rh, g, omega.

levels (hPa): 1000  925  850  775  700  500  400  300  250
              200 150  100   70   50   30   20   10    3.

Frequency: every 6 hours [0, 6, 12, 18,...,168].

Usar essas informações para ajudar a definição das variáveis (date,vars,levels,steps)


## Exemplos Python

Setar as variáveis dentro dos exemplos antes de rodar.

>python get_data_oper.py
>
>python get_netcdf.py
>
>python plot_figure.py

## Exemplos Jupyter Notebook

conda install -c anaconda ipykernel

pip install jupyter

jupyter notebook

>Example_lib.ipynb
>
>Example_lib_Widgets.ipynb
>
>Example_lib_regrid.ipynb
