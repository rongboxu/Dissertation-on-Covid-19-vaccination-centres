# Dissertation-on-Covid-19-vaccination-centres

This repository contains codes and data of the dissertation, 'Location Optimisation of Covid-19 Vaccination Sites: A Case Study of England'.  

Key Steps and Codes

1. Case study 1: run **LSCP easy example.ipynb** in **0713update**
2. Case study 2:
1) original Location Set Covering Problem(LSCP) model: run **original_LSCP.ipynb** in **LSCP_code**
2) least-relocation LSCP model: run **new_least_relocation_LSCP.ipynb** in **LSCP_code**
3) original LSCP model with constraint A and B: run **original_LSCP_constraints.ipynb** in **LSCP_code**

Data

1. For Case study 1, all in **0713update/data/**: 
1) **SF_network_distance_candidateStore_16_censusTract_205_new.csv**
2) **SF_demand_205_centroid_uniform_weight.csv**
3) **SF_store_site_16_longlat.csv**
4) **ServiceAreas_4.shp**

2. For Case study 2:
1) **distance_df_existing_sites_MSOA.csv** in **Data**
2) **distance_df_potential_sites_all_MSOA.csv** in **Data**
3) **df_existing_sites.csv** in **Huanfa**
4) **poi_three_types.csv** in **Huanfa**
