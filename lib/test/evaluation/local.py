from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/home/minhtri2001/Desktop/combine /data/got10k_lmdb'
    settings.got10k_path = '/home/minhtri2001/Desktop/combine /data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_lmdb_path = '/home/minhtri2001/Desktop/combine /data/lasot_lmdb'
    settings.lasot_path = '/home/minhtri2001/Desktop/combine /data/lasot'
    settings.network_path = '/home/minhtri2001/Desktop/combine /test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/home/minhtri2001/Desktop/combine /data/nfs'
    settings.otb_path = '/home/minhtri2001/Desktop/combine /data/OTB2015'
    settings.prj_dir = '/home/minhtri2001/Desktop/combine '
    settings.result_plot_path = '/home/minhtri2001/Desktop/combine /test/result_plots'
    settings.results_path = '/home/minhtri2001/Desktop/combine /test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/minhtri2001/Desktop/combine '
    settings.segmentation_path = '/home/minhtri2001/Desktop/combine /test/segmentation_results'
    settings.tc128_path = '/home/minhtri2001/Desktop/combine /data/TC128'
    settings.tn_packed_results_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = '/home/minhtri2001/Desktop/combine /data/trackingNet'
    settings.uav_path = '/home/minhtri2001/Desktop/combine /data/UAV123'
    settings.vot_path = '/home/minhtri2001/Desktop/combine /data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

