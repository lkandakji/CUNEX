if __name__ == '__main__':
    from nnunetv2.paths import nnUNet_results, nnUNet_raw
    import torch
    from batchgenerators.utilities.file_and_folder_operations import join
    from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
    from nnunetv2.utilities.label_handling.label_handling import LabelManager
    from PIL import Image
    import os
    import numpy as np

    # instantiate the nnUNetPredictor
    predictor = nnUNetPredictor(
        tile_step_size=0.5,
        use_gaussian=True,
        use_mirroring=True,
        perform_everything_on_device=True,

        device=torch.device('cpu'), # CHANGE TO GPU IF AVAILABLE
        verbose=False,
        verbose_preprocessing=False,
        allow_tqdm=True
    )
    
    predictor.label_manager_class = LabelManager
    
    # initializes the network architecture, loads the checkpoint
    predictor.initialize_from_trained_model_folder(
        '2d_fullres path', # REPLACE
        use_folds=(0,),
        checkpoint_name='cunex.pth',
    )
    
    # variant 1: give input and output folders
    predicted_segmentations = predictor.predict_from_files(join(nnUNet_raw, 'imagesTs_renamed path here'),
                                 join(nnUNet_raw, 'imagesTs_pred path here'),
                                 save_probabilities=False, overwrite=False,
                                 num_processes_preprocessing=2, num_processes_segmentation_export=2,
                                 folder_with_segs_from_prev_stage=None, num_parts=1, part_id=0)

    # to see the masks
    input_dir = "imagesTs_pred path here"
    output_dir = input_dir + "_vis"

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            arr = np.array(img)
            # Multiply by 255 to make classes visible
            vis_arr = (arr * 255).astype(np.uint8)
            vis_img = Image.fromarray(vis_arr)
            vis_img.save(os.path.join(output_dir, filename))
