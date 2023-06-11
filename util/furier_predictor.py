import numpy as np

def create_fourier_predictor(data, num_terms):
    num_samples = len(data)
    frequencies = np.fft.fftfreq(num_samples)
    fft_values = np.fft.fft(data)
    
    def fourier_series(t):
        f_approx = np.zeros_like(t, dtype=complex)
        for n in range(num_terms):
            coef = fft_values[n] / num_samples
            f_approx += coef * np.exp(1j * 2 * np.pi * frequencies[n] * t)
        real_part = np.real(f_approx)
        return real_part
    
    return fourier_series