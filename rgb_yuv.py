
def rgb_to_yuv(r,g,b):
    y = 0.257 *r + 0.504 * g + 0.098 * b +16 ;
    u =-0.148 *r - 0.291*g +0.439*b+128;
    v = 0.439 *r -0.368*g -0.071 *b+128;
    return y,u,v

def yuv_to_rgb(y,u,v):
    #import pdb;pdb.set_trace() #debug
    r = 1.164 * (y-16)+ 1.596*(v-128);
    g = 1.164 *(y-16) - 0.813 *(v-128) - 0.391 * (u-128);
    b = 1.164 * (y-16) + 2.018 * (u-128);
    return r, g, b

if __name__ == '__main__':
    r_ori = input("Introduce un valor R: ");
    g_ori = input("Introduce un valor G: ");
    b_ori = input("Introduce un valor B: ");

    y,u,v = rgb_to_yuv(r_ori,g_ori,b_ori)
    r,g,b = yuv_to_rgb(y,u,v)

    print("YUV valores son",y,u,v);
    print("RGB valores son",r,g,b);

