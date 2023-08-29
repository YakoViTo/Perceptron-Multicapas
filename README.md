# Perceptrón Multicapas

The problem consists of classifying random two-dimensional points located on a 4x4 chessboard, which is contained in a rectangle of dimensions [0, 10] x [0, 10]. The points on the board are distributed in red and white squares, and the task is to label these points according to the color of the square in which they fall. Dots in red squares should be labeled -1, and dots in white squares should be labeled 1.

The solution consists of implementing a multilayer perceptron to classify the points on the board. A random data of points in the rectangle [0, 10] x [0, 10] is generated, and then these points are labeled according to the color of the board square in which they fall. The multilayer perceptron is trained with this data and learns to classify the dots into red or white squares. After training, the chessboard is displayed along with the classified points.

It is important to point out that Python version 3.10.5 under Windows 10 was used for the solution to the problem posed; the NumPy libraries were also enabled to generate data, manipulate matrices and perform numerical operations related to the multilayer perceptron and sklearn, which is a very useful tool for applying automatic learning techniques, including the use of multilayer perceptrons for classification; the Matplotlib library was also incorporated to better appreciate the results by means of graphs.

![image](https://github.com/YakoViTo/Perceptron-Multicapas/assets/135473233/24d4b465-92a2-41e0-b950-ba5fcd58ba2e)

After training the multilayer perceptron, different results will be obtained in each run due to the random generation of the data. And visualizing the dashboard along with the ranked points will allow observing how the network has learned to separate the red and white squares.

With the given architecture and data set, the multilayer perceptron is likely to achieve high classification accuracy due to the simplicity of the problem and the relatively small size of the board. However, in more complex problems, larger network architectures and larger data sets may be required to obtain accurate results and avoid overfitting.

Experiment with different parameters and distributions so that you can better understand how these aspects affect model performance.
