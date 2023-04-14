from spatialdata import SpatialData
import torch
import torch.nn.functional as F

CELL_TYPES = ['B-cells', 'CAFs', 'Cancer Epithelial', 'Endothelial', 'Myeloid', 'Normal Epithelial', 'PVL', 'Plasmablasts', 'T-cells']

def my_transform(sdata: SpatialData) -> tuple[torch.tensor, torch.tensor]:
    tile = sdata['CytAssist_FFPE_Human_Breast_Cancer_full_image'].data.compute()
    tile = torch.tensor(tile).float()
    
    expected_category = sdata.table.obs['celltype_major'].values[0]
    expected_category = CELL_TYPES.index(expected_category)
    cell_type = F.one_hot(
        torch.tensor(expected_category), num_classes=len(CELL_TYPES)
    ).float()
    return tile, cell_type
