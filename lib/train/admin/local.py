class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/minhtri2001/Desktop/combine '    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/minhtri2001/Desktop/combine /tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/minhtri2001/Desktop/combine /pretrained_networks'
        self.lasot_dir = '/home/minhtri2001/Desktop/combine /data/lasot'
        self.got10k_dir = '/home/minhtri2001/Desktop/combine /data/got10k'
        self.lasot_lmdb_dir = '/home/minhtri2001/Desktop/combine /data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/minhtri2001/Desktop/combine /data/got10k_lmdb'
        self.trackingnet_dir = '/home/minhtri2001/Desktop/combine /data/trackingnet'
        self.trackingnet_lmdb_dir = '/home/minhtri2001/Desktop/combine /data/trackingnet_lmdb'
        self.coco_dir = '/home/minhtri2001/Desktop/combine /data/coco'
        self.coco_lmdb_dir = '/home/minhtri2001/Desktop/combine /data/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/minhtri2001/Desktop/combine /data/vid'
        self.imagenet_lmdb_dir = '/home/minhtri2001/Desktop/combine /data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
