import subsaz.CPTEC_SUB as SUB
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Inicializa o construtor
sub = SUB.model()
# Filtrar area Brasil
sub.dict['area']['reduce'] = True 
sub.dict['area']['minlat'] = -34.44
sub.dict['area']['maxlat'] = -21.43
sub.dict['area']['minlon'] = 301.14
sub.dict['area']['maxlon'] = 320.57
# Requisição dos dados
f = sub.load(date='20230104', var='prec', step='01', product='week' ,field='anomalies')
# Definir tamanho da figura
fig = plt.figure(figsize=(10,8))
# Setar figura unica
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
# Colocar  Linhas de Borda dos paises e linhas costeiras
ax.add_feature(cfeature.COASTLINE,color='grey')
ax.add_feature(cfeature.BORDERS,color='grey')
# Definir Regiao do Brasil
ax.set_extent([-90,-30,10,-41], ccrs.PlateCarree())
# Setar estados do Brasil
states = cfeature.NaturalEarthFeature(category='cultural',
                                            name='admin_1_states_provinces_lines',
                                            scale='50m', facecolor='none')
# Colocar Estados Brasil
ax.add_feature(states, edgecolor='gray')
# Plotar variavel
f.prec.plot()
plt.show()
