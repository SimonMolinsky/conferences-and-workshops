import rasterio as rio
import rasterio.mask as rmask

def clip_area(vector_geometry, raster_file, save_image_to):

    with rio.open(raster_file, 'r') as raster_source:
        clipped_image, transform = rmask.mask(raster_source, vector_geometry, crop=True)
        metadata = raster_source.meta.copy()
        
    metadata.update({"driver": "GTiff",
                 "height": clipped_image.shape[1],
                 "width": clipped_image.shape[2],
                 "transform": transform})
    with rio.open(save_image_to, "w", **metadata) as g_tiff:
        g_tiff.write(clipped_image)