# -*- coding: utf-8 -*-

from NeuralNetwork import NeuralNetwork
from gradientVerification import verifGradient1d, verifGradientKd
import utils
import numpy as np


def main():
    print("\n\n>>EXERCICE 1 et 2")
    sigma = 1e-4
    neuralNetwork = NeuralNetwork(2, 2, 2)
    X = [0.4, 0.7]
    y = 1  # imaginons que c'est un point de la classe
    print("Liste des ratio W1, b1, W2, b2")
    res = verifGradient1d(neuralNetwork, X, y)
    print(res)
    print(">Tout les ratio sont bien entre 0.99 et 1.01" if False not in [0.99 < i < 1.01 for i in (
    np.array(res)).flatten()] else "Echec de la verif..")

    print("\n\n>>EXERCICE 3 et 4")
    neuralNetwork = NeuralNetwork(2, 2, 2)
    X, y = utils.readMoonFile()
    K = 10
    X = X[:K]
    y = y[:K]

    print("Liste des ratio W1, b1, W2, b2")
    res = verifGradientKd(neuralNetwork, X, y)
    print(res)
    print(">Tout les ratio sont bien entre 0.99 et 1.01" if False not in [0.99 < i < 1.01 for i in (
    np.array(res)).flatten()] else "Echec de la verif..")

    print("\n\n>>EXERCICE 5 Entrainement du reseau de neuronne + Variation des hyper-parametres")
    X, y = utils.readMoonFile()

    default_h = 5
    sample_h = [2, 5, 10, 100, 1000]

    default_wd = 0.1
    sample_wd = [0, 0.00001, 0.0001, 0.001,
                 0.01]  # todo Valider terme de regularisation dans NeuralNetwork. Lorsque != 0, validations #1,2,3,4 ne sont plus bon...

    default_maxIter = 5
    sample_maxIter = [1, 2, 5, 10, 20]

    for h in sample_h:
        neuralNetwork = NeuralNetwork(len(X[0]),h,utils.getClassCount(y),default_wd)
        neuralNetwork.train(X, y, default_maxIter)
        predictions = neuralNetwork.computePredictions(X)

        trainEfficiency = utils.calculatePredictionsEfficiency(predictions, y)
        title = "h: " + str(h) + " / wd: " + str(default_wd) + " / " + str(
            default_maxIter) + " epoques" + " / Train Err: " + str(100 - trainEfficiency) + "%"
        name = "regions_decision" + str(h) + "_" + str(default_wd) + "_" + str(default_maxIter)
        utils.plotRegionsDescision(X, y, neuralNetwork, title, name)

    for wd in sample_wd:
        neuralNetwork = NeuralNetwork(len(X[0]),default_h,utils.getClassCount(y),wd)
        neuralNetwork.train(X, y, default_maxIter)
        predictions = neuralNetwork.computePredictions(X)

        trainEfficiency = utils.calculatePredictionsEfficiency(predictions, y)
        title = "h: " + str(default_h) + " / wd: " + str(wd) + " / " + str(
            default_maxIter) + " epoques" + " / Train Err: " + str(100 - trainEfficiency) + "%"
        name = "regions_decision" + str(default_h) + "_" + str(wd) + "_" + str(default_maxIter)
        utils.plotRegionsDescision(X, y, neuralNetwork, title, name)

    for maxIter in sample_maxIter:
        neuralNetwork = NeuralNetwork(len(X[0]),default_h,utils.getClassCount(y),default_wd)
        neuralNetwork.train(X, y, maxIter)
        predictions = neuralNetwork.computePredictions(X)

        trainEfficiency = utils.calculatePredictionsEfficiency(predictions, y)
        title = "h: " + str(default_h) + " / wd: " + str(default_wd) + " / " + str(
            maxIter) + " epoques" + " / Train Err: " + str(100 - trainEfficiency) + "%"
        name = "regions_decision" + str(default_h) + "_" + str(default_wd) + "_" + str(maxIter)
        utils.plotRegionsDescision(X, y, neuralNetwork, title, name)


if __name__ == '__main__':
    main()
