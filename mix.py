import os
import sys
import pickle
import numpy as np
import PIL.Image
import dnnlib
import dnnlib.tflib as tflib
import config
import random

# python mix.py "number".jpg


GENERATED_IMAGE_JPEG = sys.argv[1]
GENERATED_IMAGE_NUM = os.path.splitext(GENERATED_IMAGE_JPEG)[0]
print(GENERATED_IMAGE_NUM)
# url_ffhq = 'https://drive.google.com/uc?id=1MEGjdvVpUsu1jB4zrXZN7Y4kBBOzizDQ'
fpath = './karras2019stylegan-ffhq-1024x1024.pkl'
synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True), minibatch_size=8)
_Gs_cache = dict()

def load_Gs(url):
    # if url not in _Gs_cache:
    #     with dnnlib.util.open_url(url, cache_dir=config.cache_dir) as f:
    #         _G, _D, Gs = pickle.load(f)
    #     _Gs_cache[url] = Gs
    # return _Gs_cache[url]
    with open(fpath, mode='rb') as f:
        _G, _D, Gs = pickle.load(f)
    return Gs

def draw_style_mixing_figure(png, Gs, w, h, src_seeds, dst_seeds, style_ranges):
    # print(png)
    src_latents = np.stack(np.random.RandomState(seed).randn(Gs.input_shape[1]) for seed in src_seeds)
#    dst_latents = np.stack(np.random.RandomState(seed).randn(Gs.input_shape[1]) for seed in dst_seeds)
    src_dlatents = Gs.components.mapping.run(src_latents, None) # [seed, layer, component]
#    dst_dlatents = Gs.components.mapping.run(dst_latents, None) # [seed, layer, component]

    # dlatents = np.load('./latent/miyano.npy')
    dlatents = np.load('./latent/' + GENERATED_IMAGE_NUM + '.npy')
    # dst_dlatents = np.zeros((3,18,512))
    dst_dlatents = np.zeros((1,18,512))
    dst_dlatents[0] = dlatents
    # dst_dlatents[1] = dlatents
    # dst_dlatents[2] = dlatents
    # print(dst_dlatents.shape)

    src_images = Gs.components.synthesis.run(src_dlatents, randomize_noise=False, **synthesis_kwargs)
    dst_images = Gs.components.synthesis.run(dst_dlatents, randomize_noise=False, **synthesis_kwargs)

    # canvas = PIL.Image.new('RGB', (w * (len(src_seeds) + 1), h * (len(dst_seeds) + 1)), 'white')
    # for col, src_image in enumerate(list(src_images)):
    #     canvas.paste(PIL.Image.fromarray(src_image, 'RGB'), ((col + 1) * w, 0))
    # for row, dst_image in enumerate(list(dst_images)):
    #     canvas.paste(PIL.Image.fromarray(dst_image, 'RGB'), (0, (row + 1) * h))
    #     row_dlatents = np.stack([dst_dlatents[row]] * len(src_seeds))
    #     row_dlatents[:, style_ranges[row]] = src_dlatents[:, style_ranges[row]]
    #     row_images = Gs.components.synthesis.run(row_dlatents, randomize_noise=False, **synthesis_kwargs)
    #     for col, image in enumerate(list(row_images)):
    #         canvas.paste(PIL.Image.fromarray(image, 'RGB'), ((col + 1) * w, (row + 1) * h))
    # canvas.save(png)

    ### output 1 image

    canvas = PIL.Image.new('RGB', (w, h))
    for row, dst_image in enumerate(list(dst_images)):
        row_dlatents = np.stack([dst_dlatents[row]] * len(src_seeds))
        row_dlatents[:, style_ranges[row]] = src_dlatents[:, style_ranges[row]]
        row_images = Gs.components.synthesis.run(row_dlatents, randomize_noise=False, **synthesis_kwargs)
        for col, image in enumerate(list(row_images)):
            canvas.paste(PIL.Image.fromarray(image, 'RGB'))
    canvas.save(png)

def main():
    tflib.init_tf()
    os.makedirs(config.result_dir, exist_ok=True)
    # draw_style_mixing_figure(os.path.join(config.result_dir, 'style-mixing.png'), 
    #                          load_Gs(fpath), w=1024, h=1024, src_seeds=[639,701,687,615,2268], dst_seeds=[0,0,0],
    #                         #  load_Gs(url_ffhq), w=1024, h=1024, src_seeds=[1000], dst_seeds=[0,0,0],
    #                          style_ranges=[range(0,4)]+[range(4,8)]+[range(8,18)])

    # father father images
    """
    12, 103, 114, 145, 189, 196, 218, 221, 240, 247, 248, 265, 23992, 23962, 23937, 23923, 23918, 23880, 23770
    """
    fathers_list = [12, 23756, 23880, 23908, 23992, 265, 23770, 56, 189, 2760, 257, 23962]
    father_src = random.choice(fathers_list)
    draw_style_mixing_figure(os.path.join('./father_imgs', GENERATED_IMAGE_NUM + '.jpg'), 
                             load_Gs(fpath), w=1024, h=1024, src_seeds=[father_src], dst_seeds=[0,0,0],
                             style_ranges=[range(0,4)]+[range(4,8)]+[range(8,18)])
    # generate mother images
    """
    119, 122, 128, 129, 134, 200, 222, 236, 251, 257, 266, 23967, 23958, 23908, 23866, 23854, 23756, 23741, 23740
    """
    mothers_list = [221, 134, 23740, 11111, 266, 5423, 23923, 23741, 1231, 342, 248, 3120]
    mother_src = random.choice(mothers_list)
    draw_style_mixing_figure(os.path.join('./mother_imgs', GENERATED_IMAGE_NUM + '.jpg'), 
                             load_Gs(fpath), w=1024, h=1024, src_seeds=[mother_src], dst_seeds=[0,0,0],
                             style_ranges=[range(0,4)]+[range(4,8)]+[range(8,18)])

    print("Done image mixed")

if __name__ == "__main__":
    main()