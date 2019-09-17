#include <iostream>
#include <libyuv.h>
#include <string.h>

int main(int argc, char* argv[])
{
    std::cout << "Version: " << LIBYUV_VERSION << std::endl;

    const int kWidth = 16;
    const int kHeight = 1;
    const int kPixels = kWidth * kHeight;

    uint8_t orig_y[16];
    uint8_t y[16];
    uint8_t orig_pixels[16 * 4];
    memset(orig_y, 0, kPixels);

    /* YUV converted to ARGB. */
    libyuv::I400ToARGB(orig_y, kWidth, orig_pixels, kWidth * 4, kWidth, kHeight);


    return 0;
}