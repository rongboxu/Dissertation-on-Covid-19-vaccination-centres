def add_projected_XY(df_points, col_x, col_y, new_col_x, new_col_y, current_crs='epsg:4326', new_crs='epsg:27700'):
    
    import geopandas
    df_points_cp = df_points.copy()
    gdf_projected = geopandas.GeoDataFrame(df_points_cp, geometry=geopandas.points_from_xy(df_points_cp[col_x], df_points_cp[col_y]))
    # wgs84
    gdf_projected.crs = current_crs
    gdf_projected = gdf_projected.to_crs(new_crs)

    df_points_cp[new_col_x] =  gdf_projected.geometry.x
    df_points_cp[new_col_y] =  gdf_projected.geometry.y
    return df_points_cp