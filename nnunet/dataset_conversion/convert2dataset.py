from copy import deepcopy
from pathlib import Path
from batchgenerators.utilities.file_and_folder_operations import *
import shutil



if __name__ == "__main__":
	labels_base = "/Volumes/anxingle/datasets/SegUncLabels/test1-final/"
	out = "/media/fabian/My Book/MedicalDecathlon/nnUNet_raw_splitted/Task040_KiTS"

	json_dict = {}
	json_dict['name'] = "MyData"
	json_dict['description'] = "Use nnUNet to train"
	json_dict['tensorImageSize'] = "4D"
	json_dict['reference'] = "KiTS data for nnunet"
	json_dict['licence'] = ""
	json_dict['release'] = "0.0"
	json_dict['modality'] = {
		"0": "CT",
	}
	json_dict['labels'] = {
		"0": "background",
		"1": "Kidney",
		"2": "Tumor"
	}

	cases = [f.name for f in Path(labels_base).iterdir() if f.is_file() and ".nii.gz" in f.name]
	json_dict['numTraining'] = len(cases)
	json_dict['numTest'] = 0
	json_dict['training'] = [{'image': "./imagesTr/%s.nii.gz" % i[:-7], "label": "./labelsTr/%s.nii.gz" % i[:-7]} for i in
							 cases]
	json_dict['test'] = []

	save_json(json_dict, os.path.join(out, "dataset.json"))
