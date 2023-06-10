
Fouerier Transform
==================
Introduction:

The Fourier Transform is a mathematical tool used extensively in digital signal processing for analyzing signals in terms of their frequency content. It converts a time-domain waveform into its frequency-domain representation. Python has several libraries that implement the Fourier transform algorithm. This course will cover how to use the Fourier Transform in Python version 3.10 with the numpy and matplotlib libraries.

Prerequisites:

To understand this course, you need to have a basic understanding of Python and programming concepts like loops and conditional statements. Also, knowledge of mathematics concepts like Fourier series and transforms will help you understand the concepts better.

Step 1: Installing Required Libraries

The first step is to install the required libraries numpy and matplotlib. You can install them using pip with the following command:

```python
pip install numpy matplotlib
```

Step 2: Importing Required Libraries

To use the Fourier transform in Python, we need to import the numpy and matplotlib libraries. The numpy library provides efficient arrays and functions for numerical computations. The matplotlib library provides functions for plotting graphs and visualizations.

```python
import numpy as np
import matplotlib.pyplot as plt
```

Step 3: Creating a Sample Signal

We will create a sample signal to demonstrate the Fourier transform function. We will generate a signal with a sum of frequencies using the numpy library's sine and cosine functions.

```python
t = np.linspace(0, 2*np.pi, 1000)  # Generating time variable
signal = 10 * np.sin(5*t) + 5 * np.cos(10*t) + 2 * np.sin(20*t) # Generating signal
plt.plot(t, signal) # Plotting Signal
plt.show() # Display plot
```

Output:

![sample signal plot](https://i.imgur.com/OrUpPEG.png)


Step 4: Performing Fourier Transform

To perform Fourier transformation, we can call np.fft function from the numpy library. np.fft returns an array of complex numbers, which contains the Fourier series coefficients of the input signal.

```python
fourier_coeffs = np.fft.fft(signal)  # Performing Fourier Transform
```

The output of the Fourier transform is an array of complex numbers. These complex numbers represent the Fourier coefficients for each frequency component present in the input signal. The amplitude of the complex number represents the magnitude of the frequency component's contribution, and the angle of the complex number represents the phase of the component. We can use np.abs to get the magnitude of the Fourier coefficients and np.angle to get the phase.

```python
fourier_magnitudes = np.abs(fourier_coeffs)  # Magnitude of Fourier Coefficients
fourier_phases = np.angle(fourier_coeffs)  # Phase of Fourier Coefficients
```

The magnitude and phase can be plotted using the following code.

```python
freqs = np.fft.fftfreq(signal.size, t[1]-t[0])  # Generating Frequency domain variable (Hz)
plt.plot(freqs, fourier_magnitudes) # Plotting Magnitude
plt.xlabel("Frequency (Hz)") # Label x-axis
plt.ylabel("Magnitude") # Label y-axis
plt.show() # Display plot

plt.plot(freqs, fourier_phases) # Plotting Phase
plt.xlabel("Frequency (Hz)") # Label x-axis
plt.ylabel("Phase") # Label y-axis
plt.show() # Display plot
```

Output:

![frequency-magnitude plot](https://i.imgur.com/hPeWeh3.png)

![frequency-phase plot](https://i.imgur.com/wZWhLoC.png)


Step 5: Applying Inverse Fourier Transform

If we have the Fourier coefficients, we can also apply an inverse Fourier transform to convert the Fourier coefficients back to the time domain signal.

```python
reconstructed_signal = np.fft.ifft(fourier_coeffs)  # Performing Inverse Fourier Transform
plt.plot(t, reconstructed_signal)  # Plotting reconstructed signal
plt.show()  # Display plot
```

Output:

![reconstructed signal plot](https://i.imgur.com/FNwEUARK.png)


Conclusion:

In this course, we learned how to use the Fourier transform in Python version 3.10. We also learned how to use numpy and matplotlib to generate, perform Fourier transform, and visualize signals. The Fourier transform has many applications, including signal processing, image processing, and processing audio signals. Congratulations on completing the course.