import time
inicio = time.time()
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
#Lendo os arquivos csv e criando dataframes para serem tratados
df_PROUNI_2016= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2016_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2015= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2015_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2014= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2014_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2013= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2013_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2012= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2012_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2011= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2011_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2010= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2010_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2009= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2009_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2008= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2008_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2007= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2007_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2006= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2006_CSV.CSV', sep=';', encoding='latin-1')
df_PROUNI_2005= pd.read_csv('/Users/Blueshift014/Documents/Base Prouni/PDA_PROUNI_2005_CSV.CSV', sep=';', encoding='latin-1')
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % round(fim - inicio))

inicio = time.time()
#Concatenando todos os arquivos para criação de uma única base
df_PROUNI_Historico = pd.concat([df_PROUNI_2016,df_PROUNI_2015,df_PROUNI_2014, df_PROUNI_2013, df_PROUNI_2012, df_PROUNI_2011, 
                                 df_PROUNI_2010, df_PROUNI_2009, df_PROUNI_2008, df_PROUNI_2007, df_PROUNI_2006, df_PROUNI_2005])
#Gerando os dataframes por cidades para depois gerar o dataframe do CIMBAJU
df_PROUNI_MORATO = df_PROUNI_Historico[(df_PROUNI_Historico['MUNICIPIO_BENEFICIARIO_BOLSA']=='FRANCISCO MORATO')]
df_PROUNI_CAIEIRAS = df_PROUNI_Historico[(df_PROUNI_Historico['MUNICIPIO_BENEFICIARIO_BOLSA']=='CAIEIRAS')]
df_PROUNI_FRANCO_DA_ROCHA = df_PROUNI_Historico[(df_PROUNI_Historico['MUNICIPIO_BENEFICIARIO_BOLSA']=='FRANCO DA ROCHA')]
df_PROUNI_CAJAMAR = df_PROUNI_Historico[(df_PROUNI_Historico['MUNICIPIO_BENEFICIARIO_BOLSA']=='CAJAMAR')]
df_PROUNI_MAIRIPORA = df_PROUNI_Historico[(df_PROUNI_Historico['MUNICIPIO_BENEFICIARIO_BOLSA']=='MAIRIPORÃ')]
#Criação do dataframe CIMBAJU com a composição dos dados integrais das cidades de: Francisco Morato, Franco da Rocha, Caieiras,
#Cajamar e Mairiporã
df_PROUNI_CIMBAJU = pd.concat([df_PROUNI_MORATO, df_PROUNI_CAIEIRAS, df_PROUNI_FRANCO_DA_ROCHA, 
               df_PROUNI_CAJAMAR, df_PROUNI_MAIRIPORA])
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % round(fim - inicio))

inicio = time.time()
#Total de bolsas concedidas no Brasil
brasil = df_PROUNI_Historico['ANO_CONCESSAO_BOLSA'].count()
print('Total de bolsas concedidas no Brasil: %2.0f' %(brasil))
#Total de bolsas concedidas no CIMBAJU
cimbaju = df_PROUNI_CIMBAJU['ANO_CONCESSAO_BOLSA'].count()
print('Total de bolsas concedidas no CIMBAJU: %2.0f' %(cimbaju))
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#linha de codigo que plota grafico do tipo de bolsa em formato de barra e mostra a quantidade
df_PROUNI_Historico.groupby('ANO_CONCESSAO_BOLSA').count().plot(kind ='bar', 
figsize =(12,5), grid=False, rot =0, color = 'green', legend=False)
plt.title('Quantidade de bolsas concedidas de 2005-2016')
plt.xlabel('Ano de concessão')
plt.ylabel('Quantidade no período')
plt.show()
print(df_PROUNI_Historico['ANO_CONCESSAO_BOLSA'].value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#linha de codigo que plota grafico do tipo de bolsa em formato de barra e mostra a quantidade
df_PROUNI_CIMBAJU.groupby('ANO_CONCESSAO_BOLSA').count().plot(kind ='bar', 
figsize =(12,5), grid=False, rot =0, color = 'green', legend=False)
plt.title('Quantidade de bolsas concedidas de 2005-2016')
plt.xlabel('Ano de concessão')
plt.ylabel('Quantidade no período')
plt.show()
print(df_PROUNI_CIMBAJU['ANO_CONCESSAO_BOLSA'].value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#Top 5 das instituições no Brasil
df_bi = df_PROUNI_Historico.loc[df_PROUNI_Historico['TIPO_BOLSA'] == 'BOLSA INTEGRAL']
df_bi['NOME_IES_BOLSA'].value_counts().sort_values(ascending=False).head(5).plot(kind ='barh', 
figsize =(10,5), grid=False, rot =0, color = 'green', legend=False)
plt.title('Top 5 das instituicoes de 2005-2016 no Brasil')
plt.xlabel('Quantidade de bolsa')
plt.show()
print(df_bi['NOME_IES_BOLSA'].value_counts().sort_values(ascending=False).head(5))
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#Top 5 das instituições no CIMBAJU
df_bi = df_PROUNI_CIMBAJU.loc[df_PROUNI_CIMBAJU['TIPO_BOLSA'] == 'BOLSA INTEGRAL']
df_bi['NOME_IES_BOLSA'].value_counts().sort_values(ascending=False).head(5).plot(kind ='barh', 
figsize =(10,5), grid=False, rot =0, color = 'green', legend=False)
plt.title('Top 5 das instituicoes de 2005-2016 no CIMBAJU')
plt.xlabel('Quantidade de bolsa')
plt.show()
print(df_bi['NOME_IES_BOLSA'].value_counts().sort_values(ascending=False).head(5))
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#bolsas concedidas por região
df_PROUNI_Historico.groupby('REGIAO_BENEFICIARIO_BOLSA').count().plot(kind ='bar', 
figsize =(12,5), grid=False, rot =0, color = 'green', legend=False)
plt.title('Quantidade de bolsas concedidas por regiao de 2005-2016')
plt.xlabel('Regiao')
plt.ylabel('Quantidade no período')
plt.show()
print(df_PROUNI_Historico['REGIAO_BENEFICIARIO_BOLSA'].value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#bolsas concedidas por Cidade no CIMBAJU
df_PROUNI_CIMBAJU.groupby('MUNICIPIO_BENEFICIARIO_BOLSA').count().plot(kind ='bar', 
figsize =(12,5), grid=False, rot =0, color = 'green', legend=False)
plt.title('Quantidade de bolsas concedidas por cidade de 2005-2016')
plt.xlabel('Regiao')
plt.ylabel('Quantidade no período')
plt.show()
print(df_PROUNI_CIMBAJU['MUNICIPIO_BENEFICIARIO_BOLSA'].value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
# concessões por sexo no Brasil
df_PROUNI_Historico.SEXO_BENEFICIARIO_BOLSA.value_counts().plot(kind='pie'
,autopct='%.2f%%')
plt.axis('equal')# Para deixar o gráfico redondo
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
# concessões pessoas com deficiencia no Brasil
df_PROUNI_Historico.BENEFICIARIO_DEFICIENTE_FISICO.value_counts().plot(kind='pie'
,autopct='%.2f%%')
plt.axis('equal')# Para deixar o gráfico redondo
print(df_PROUNI_Historico.BENEFICIARIO_DEFICIENTE_FISICO.value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
# concessões por sexo no CIMBAJU
df_PROUNI_CIMBAJU.SEXO_BENEFICIARIO_BOLSA.value_counts().plot(kind='pie'
,autopct='%.2f%%')
plt.axis('equal')# Para deixar o gráfico redondo
print(df_PROUNI_CIMBAJU.SEXO_BENEFICIARIO_BOLSA.value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
# concessões por pessoas com deficiencia no CIMBAJU
df_PROUNI_CIMBAJU.BENEFICIARIO_DEFICIENTE_FISICO.value_counts().plot(kind='pie'
,autopct='%.2f%%')
plt.axis('equal')# Para deixar o gráfico redondo
print(df_PROUNI_CIMBAJU.BENEFICIARIO_DEFICIENTE_FISICO.value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
# top 5 dos cursos por regiao no Brasil
df_cursos_x_cidades.rename(columns={"All": "Total"}, inplace=True)
df_cursos_x_cidades = pd.crosstab(df_PROUNI_Historico["NOME_CURSO_BOLSA"],
df_PROUNI_Historico["REGIAO_BENEFICIARIO_BOLSA"],
margins=True).sort_values(by='All', ascending = False).head(6)
df_cursos_x_cidades.drop('All').plot(kind = 'bar', figsize=(11,4),
title='TOP 5 Cursos por regiao do Brasil', legend=True)
df_cursos_x_cidades.rename(columns={"All": "Total"}, inplace=True)
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
# top 5 cursos por cidade no CIMBAJU
df_cursos_x_cidades.rename(columns={"All": "Total"}, inplace=True)
df_cursos_x_cidades = pd.crosstab(df_PROUNI_CIMBAJU["NOME_CURSO_BOLSA"],
df_PROUNI_CIMBAJU["MUNICIPIO_BENEFICIARIO_BOLSA"],
margins=True).sort_values(by='All', ascending = False).head(5)
df_cursos_x_cidades.drop('All').plot(kind = 'bar', figsize=(11,4),
title='CIMBAJU TOP 5 Cursos', legend=True)
df_cursos_x_cidades.rename(columns={"All": "Total"}, inplace=True)
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#Bolsas concedidas por raça no Brasil
df_PROUNI_Historico['RACA_BENEFICIARIO_BOLSA'].value_counts().plot(kind ='bar',
figsize =(12,4), grid=False, rot =0, color = 'green',legend=False)
plt.title('Quantidade de bolsistas por raça no Brasil 2005-2016')
plt.xlabel('Raça')
plt.ylabel('Quantidade no período')
plt.show()
print(df_PROUNI_Historico['RACA_BENEFICIARIO_BOLSA'].value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

inicio = time.time()
#Bolsas concedidas por raça no CIMBAJU
df_PROUNI_CIMBAJU['RACA_BENEFICIARIO_BOLSA'].value_counts().plot(kind ='bar',
figsize =(12,4), grid=False, rot =0, color = 'green',legend=False)
plt.title('Quantidade de bolsistas por raça na região do CIMBAJU 2005-2016')
plt.xlabel('Raça')
plt.ylabel('Quantidade no período')
plt.show()
print(df_PROUNI_CIMBAJU['RACA_BENEFICIARIO_BOLSA'].value_counts())
fim = time.time()
print ('duracao do processamento em segundos: %3.2f' % (fim - inicio))

#Obrigado
