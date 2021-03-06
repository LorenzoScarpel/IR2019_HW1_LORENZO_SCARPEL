#extracting data from evaluation files
PS_BM25_map_all = 0
PS_BM25_rprec_all = 0
PS_BM25_p10_all = 0
PS_BM25_ap_per_query = []
PS_BM25_rprec_per_query = []
PS_BM25_p10_per_query = []
PS_BM25_measures = open("PS_BM25.eval")
for l in PS_BM25_measures:
  measure, query, value = l.split()
  if(query == "all"):
    if(measure == "map"):
      PS_BM25_map_all = float(value)
    elif(measure == "Rprec"):
      PS_BM25_rprec_all = float(value)
    elif(measure == "P_10"):
      PS_BM25_p10_all = float(value)
  else:
    if(measure == "map"):
      PS_BM25_ap_per_query.append(float(value))
    elif(measure == "Rprec"):
      PS_BM25_rprec_per_query.append(float(value))
    elif(measure == "P_10"):
      PS_BM25_p10_per_query.append(float(value))
print ("PS_BM25_map_all: " + str(PS_BM25_map_all) + "\n" + "PS_BM25_rprec_all: " 
       + str(PS_BM25_rprec_all) + "\n" + "PS_BM25_p10_all: " + str(PS_BM25_p10_all) + "\n")
      
SL_PS_BM25_map_all = 0
SL_PS_BM25_rprec_all = 0
SL_PS_BM25_p10_all = 0
SL_PS_BM25_ap_per_query = []
SL_PS_BM25_rprec_per_query = []
SL_PS_BM25_p10_per_query = []
SL_PS_BM25_measures = open("SL_PS_BM25.eval")
for l in SL_PS_BM25_measures:
  measure, query, value = l.split()
  if(query == "all"):
    if(measure == "map"):
      SL_PS_BM25_map_all = float(value)
    elif(measure == "Rprec"):
      SL_PS_BM25_rprec_all = float(value)
    elif(measure == "P_10"):
      SL_PS_BM25_p10_all = float(value)
  else:
    if(measure == "map"):
      SL_PS_BM25_ap_per_query.append(float(value))
    elif(measure == "Rprec"):
      SL_PS_BM25_rprec_per_query.append(float(value))
    elif(measure == "P_10"):
      SL_PS_BM25_p10_per_query.append(float(value))
print("SL_PS_BM25_map_all: " + str(SL_PS_BM25_map_all) + "\n" + "SL_PS_BM25_rprec_all: " 
      + str(SL_PS_BM25_rprec_all) + "\n" + "SL_PS_BM25_p10_all: " + str(SL_PS_BM25_p10_all) + "\n")


      
SL_PS_TFIDF_map_all = 0
SL_PS_TFIDF_rprec_all = 0
SL_PS_TFIDF_p10_all = 0
SL_PS_TFIDF_ap_per_query = []
SL_PS_TFIDF_rprec_per_query = []
SL_PS_TFIDF_p10_per_query = []
SL_PS_TFIDF_measures = open("SL_PS_TFIDF.eval")
for l in SL_PS_TFIDF_measures:
  measure, query, value = l.split()
  if(query == "all"):
    if(measure == "map"):
      SL_PS_TFIDF_map_all = float(value)
    elif(measure == "Rprec"):
      SL_PS_TFIDF_rprec_all = float(value)
    elif(measure == "P_10"):
      SL_PS_TFIDF_p10_all = float(value)
  else:
    if(measure == "map"):
      SL_PS_TFIDF_ap_per_query.append(float(value))
    elif(measure == "Rprec"):
      SL_PS_TFIDF_rprec_per_query.append(float(value))
    elif(measure == "P_10"):
      SL_PS_TFIDF_p10_per_query.append(float(value))
print("SL_PS_TFIDF_map_all: " + str(SL_PS_TFIDF_map_all) + "\n" + "SL_PS_TFIDF_rprec_all: " 
      + str(SL_PS_TFIDF_rprec_all) + "\n" + "SL_PS_TFIDF_p10_all: " + str(SL_PS_TFIDF_p10_all) + "\n")

      
TFIDF_map_all = 0
TFIDF_rprec_all = 0
TFIDF_p10_all = 0
TFIDF_ap_per_query = []
TFIDF_rprec_per_query = []
TFIDF_p10_per_query = []
TFIDF_measures = open("TFIDF.eval")
for l in TFIDF_measures:
  measure, query, value = l.split()
  if(query == "all"):
    if(measure == "map"):
      TFIDF_map_all = float(value)
    elif(measure == "Rprec"):
      TFIDF_rprec_all = float(value)
    elif(measure == "P_10"):
      TFIDF_p10_all = float(value)
  else:
    if(measure == "map"):
      TFIDF_ap_per_query.append(float(value))
    elif(measure == "Rprec"):
      TFIDF_rprec_per_query.append(float(value))
    elif(measure == "P_10"):
      TFIDF_p10_per_query.append(float(value))
print("TFIDF_map_all: " + str(TFIDF_map_all) + "\n" + "TFIDF_rprec_all: " + str(TFIDF_rprec_all) 
      + "\n" + "TFIDF_p10_all: " + str(TFIDF_p10_all) + "\n")


#drawing boxplots for AP, Rprec, P@10
import matplotlib.pyplot as plt 

plt.boxplot([PS_BM25_ap_per_query, SL_PS_BM25_ap_per_query, SL_PS_TFIDF_ap_per_query, TFIDF_ap_per_query], vert=False,
           labels=["PS_BM25_AP", "SL_PS_BM25_AP", "SL_PS_TFIDF_AP", "TFIDF_AP"])
plt.show()

plt.boxplot([PS_BM25_rprec_per_query, SL_PS_BM25_rprec_per_query, SL_PS_TFIDF_rprec_per_query, TFIDF_rprec_per_query], vert=False,
           labels=["PS_BM25_RPREC", "SL_PS_BM25_RPREC", "SL_PS_TFIDF_RPREC", "TFIDF_RPREC"])
plt.show()

plt.boxplot([PS_BM25_p10_per_query, SL_PS_BM25_p10_per_query, SL_PS_TFIDF_p10_per_query, TFIDF_p10_per_query], vert=False,
           labels=["PS_BM25_P@10", "SL_PS_BM25_P@10", "SL_PS_TFIDF_P@10", "TFIDF_P@10"])
plt.show()

#ANOVA 1-way test, Tukey HSD test and plots
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

print("AP")
print(stats.f_oneway(PS_BM25_ap_per_query, SL_PS_BM25_ap_per_query, SL_PS_TFIDF_ap_per_query, TFIDF_ap_per_query))
hsd=pairwise_tukeyhsd([PS_BM25_ap_per_query, SL_PS_BM25_ap_per_query, SL_PS_TFIDF_ap_per_query, TFIDF_ap_per_query], 
                   ["PS_BM25", "SL_PS_BM25", "SL_PS_TFIDF", "TFIDF"])
print(hsd)
hsd.plot_simultaneous(xlabel='Average precision', ylabel='RUN').show()

print("RPREC")
print(stats.f_oneway(PS_BM25_rprec_per_query, SL_PS_BM25_rprec_per_query, SL_PS_TFIDF_rprec_per_query, TFIDF_rprec_per_query))
hsd=pairwise_tukeyhsd([PS_BM25_rprec_per_query, SL_PS_BM25_rprec_per_query, SL_PS_TFIDF_rprec_per_query, TFIDF_rprec_per_query], 
                   ["PS_BM25", "SL_PS_BM25", "SL_PS_TFIDF", "TFIDF"])
print(hsd)
hsd.plot_simultaneous(xlabel='Precision at recall base', ylabel='RUN').show()

print("P@10")
print(stats.f_oneway(PS_BM25_p10_per_query, SL_PS_BM25_p10_per_query, SL_PS_TFIDF_p10_per_query, TFIDF_p10_per_query))
hsd=pairwise_tukeyhsd([PS_BM25_p10_per_query, SL_PS_BM25_p10_per_query, SL_PS_TFIDF_p10_per_query, TFIDF_p10_per_query], 
                   ["PS_BM25", "SL_PS_BM25", "SL_PS_TFIDF", "TFIDF"])
print(hsd)
hsd.plot_simultaneous(xlabel='Precision at 10', ylabel='RUN').show()
