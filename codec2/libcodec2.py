from ctypes import *
from ctypes.util import find_library

def load_libcodec2():
    lib_files = ['codec2.dll', 'libcodec2.so']
    lib_files += ['..//codec2.dll', '..//libcodec2.so']
    lib_files += [find_library('codec2'), find_library('libcodec2')]

    dll = None

    for lib in lib_files:
        try:
            dll = CDLL(lib)
            break
        except:
            pass
    else:
        raise ImportError('Error loading libcodec2. Make sure libcodec2 '\
                          '(and all of its dependencies) are in your path')

    return dll

libcodec2 = load_libcodec2()


#defining new types for pointers
c_ubyte_p = POINTER(c_ubyte)

# we don't care about the codec2 struct and it's allocated by libcodec2, so
# we won't even bother filling it in
p_codec2 = c_void_p


#struct CODEC2 *  codec2_create(int mode);
f = libcodec2.codec2_create
f.restype, f.argtypes = p_codec2, [c_int]

#void codec2_destroy(struct CODEC2 *codec2_state);
f = libcodec2.codec2_destroy
f.argtypes = [p_codec2]

#void codec2_encode(struct CODEC2 *codec2_state, unsigned char * bits, short speech_in[]);
f = libcodec2.codec2_encode
f.argtypes = [p_codec2,c_ubyte_p,POINTER(c_short)]

#void codec2_decode(struct CODEC2 *codec2_state, short speech_out[], const unsigned char *bits);
f = libcodec2.codec2_decode
f.argtypes = [p_codec2,POINTER(c_short),c_ubyte_p]

#void codec2_decode_ber(struct CODEC2 *codec2_state, short speech_out[], const unsigned char *bits, float ber_est);
f = libcodec2.codec2_decode_ber
f.argtypes = [p_codec2,POINTER(c_short),c_ubyte_p,c_float]

#int  codec2_samples_per_frame(struct CODEC2 *codec2_state);
f = libcodec2.codec2_samples_per_frame
f.restype ,f.argtypes = c_int,[p_codec2]

#int  codec2_bits_per_frame(struct CODEC2 *codec2_state);
f = libcodec2.codec2_bits_per_frame
f.restype ,f.argtypes = c_int,[p_codec2]

#void codec2_set_lpc_post_filter(struct CODEC2 *codec2_state, int enable, int bass_boost, float beta, float gamma);
f = libcodec2.codec2_set_lpc_post_filter
f.argtypes = [p_codec2,c_int,c_int,c_float,c_float]

#int  codec2_get_spare_bit_index(struct CODEC2 *codec2_state);
f = libcodec2.codec2_get_spare_bit_index
f.restype ,f.argtypes = c_int,[p_codec2]

#int  codec2_rebuild_spare_bit(struct CODEC2 *codec2_state, int unpacked_bits[]);
f = libcodec2.codec2_rebuild_spare_bit
f.restype ,f.argtypes = c_int ,[p_codec2,]