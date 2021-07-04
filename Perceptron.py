import matplotlib.pyplot as plt

def computeY(yin, theta):
    if yin > theta:
        return 1
    elif yin < -theta:
        return -1
    else:
        return 0


def perceptron(samples, targetsVal, weights, b, alpha, theta):
    epoch=1
    errorArray = []
    while epoch <= 100:
        wChange = 0
        j = 0
        errorCount=0
        for sample in samples:
            i = 0
            yin = 0
            for x in sample:
                w = weights[i]
                i = i + 1
                # print(yin)
                yin += x * w
            # print(b)
            yin += b
            y = computeY(yin, theta)
            if y != targetsVal[j]:
                c = 0
                while c < len(weights):
                    weights[c] = weights[c] + alpha * targetsVal[j] * sample[c]  # updating weights
                    wChange = 1
                    c += 1
                errorCount += 1
                b = b + alpha * targetsVal[j]  # updating bias
            j += 1  # next target val
        errorArray.append(errorCount/len(samples)*100)

        if wChange:
            epoch += 1
        else:
            print("Weights are")
            count = 1
            for i in weights:
                print("w" + str(count) + "=" + str(i))
                count += 1
            print("Bias is: " + str(b))
            print("Total epochs are: " + str(epoch))
            break
    return errorArray


def main():
    # Exercise no.1
    b = 0
    weights = [0, 0, 0]
    alpha = 1.0
    theta = 0.1
    samples = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1]]
    targetsVal = [1, -1, -1, -1]
    print("<<<<<Exercise no.1>>>>>")
    perceptron(samples, targetsVal, weights, b, alpha, theta)

    # Exercise no.3
    samples2=[[1, 1, 1], [-1, 1, -1], [1, -1, 1], [1, -1, -1]]
    weights2=[0,0,0]
    targetsVal2=[1,1,-1,-1]
    print("\n<<<<<Exercise no.3>>>>>")
    error = perceptron(samples2, targetsVal2, weights2, b, alpha, theta)
    # print(error)

    # Displaying error in graph
    plt.plot(error)
    plt.title("Error Graph")
    plt.xlabel("epochs")
    plt.ylabel("error")
    plt.grid()
    plt.show()

main()