#include <ap_fixed.h>
#include <hls_math.h>
#include <ap_int.h>

#define IMG_SIZE 64
#define KERNEL 3
#define CHANNELS 3
#define FILTERS 8

typedef ap_fixed<16,6> data_t;

void conv2d_accel(
    data_t *input,
    data_t *kernel,
    data_t *bias,
    data_t *output
)
{

#pragma HLS INTERFACE m_axi port=input  offset=slave bundle=gmem
#pragma HLS INTERFACE m_axi port=kernel offset=slave bundle=gmem
#pragma HLS INTERFACE m_axi port=bias   offset=slave bundle=gmem
#pragma HLS INTERFACE m_axi port=output offset=slave bundle=gmem

#pragma HLS INTERFACE s_axilite port=input  bundle=control
#pragma HLS INTERFACE s_axilite port=kernel bundle=control
#pragma HLS INTERFACE s_axilite port=bias   bundle=control
#pragma HLS INTERFACE s_axilite port=output bundle=control
#pragma HLS INTERFACE s_axilite port=return bundle=control

    for(int f = 0; f < FILTERS; f++) {
        for(int i = 0; i < IMG_SIZE-KERNEL+1; i++) {
            for(int j = 0; j < IMG_SIZE-KERNEL+1; j++) {

#pragma HLS PIPELINE II=2

                data_t sum = 0;

                for(int ki = 0; ki < KERNEL; ki++) {
                    for(int kj = 0; kj < KERNEL; kj++) {
                        for(int c = 0; c < CHANNELS; c++) {

#pragma HLS UNROLL
                            int input_index =
                                ((i+ki)*IMG_SIZE + (j+kj)) * CHANNELS + c;

                            int kernel_index =
                                ((ki*KERNEL + kj) * CHANNELS + c) * FILTERS + f;

                            sum += input[input_index] * kernel[kernel_index];
                        }
                    }
                }

                int out_index =
                    (i*(IMG_SIZE-KERNEL+1) + j) * FILTERS + f;

                output[out_index] = sum + bias[f];
            }
        }
    }
}
