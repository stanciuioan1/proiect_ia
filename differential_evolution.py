from audioop import cross
import cmath
import random

SOLUTION_DIM = 2
POP_SIZE = 10
LOWER_BOUND = -1000
UPPER_BOUND = 1000
MUTATION_RATE = 0.02
CROSSOVER_PROBABILITY = 0.9
DIFFERENTIAL_FACTOR = 0.8
MAX_ERROR = 1.e-5
EQUATION = []


def evaluateFunction(z: complex):
    global EQUATION
    result = 0 + 0j
    for tup in EQUATION:
        if tup[0] == 'poly':
            result += z ** int(tup[3]) * (int(tup[1]) + int(tup[2]) * 1j)
        elif tup[0] == 'sin':
            result += cmath.sin(z) * (int(tup[1]) + int(tup[2]) * 1j)
        elif tup[0] == 'cos':
            result += cmath.cos(z) * (int(tup[1]) + int(tup[2]) * 1j)
        elif tup[0] == 'tg':
            result += cmath.tan(z) * (int(tup[1]) + int(tup[2]) * 1j)
        elif tup[0] == 'ctg':
            result += 1/cmath.tan(z) * (int(tup[1]) + int(tup[2]) * 1j)
    return result

def generatePopulation(populationSize=POP_SIZE):
    population = []
    for _ in range(populationSize):
        chrA = random.randint(LOWER_BOUND, UPPER_BOUND)
        chrB = random.randint(LOWER_BOUND, UPPER_BOUND)
        population.append([chrA, chrB])
    return population


def getEliteMember(pop):
    fittest = pop[0]
    fittestValue = abs(evaluateFunction(fittest[0] + fittest[1] * 1j))
    
    for member in pop[1:]:
        memberValue = abs(evaluateFunction(member[0] + member[1] * 1j))
        if fittestValue > memberValue:
            fittestValue = memberValue
            fittest = member
    
    return fittest


def mutate(pop):
    for member in pop:
        for i in range(len(member)):
            if random.randint(0, 100) / 100 < MUTATION_RATE:
                member[i] = random.randint(LOWER_BOUND, UPPER_BOUND)


def getMembersBesides(population, member):
    a = member
    b = member
    c = member
    while member == a or a == b or b == c:
        a = population[random.randint(0, len(population) - 1)]
        b = population[random.randint(0, len(population) - 1)]
        c = population[random.randint(0, len(population) - 1)]
    
    return a, b, c

def differentialEvolution(equation, maxEpochs=50000):
    global EQUATION
    EQUATION = equation
    population = generatePopulation()

    for currentEpoch in range(maxEpochs):
        eliteMember = getEliteMember(population)
        if currentEpoch % 100 == 0:
            print(f'Epoch #{currentEpoch}: ')
            print(f'Best solution: {eliteMember} which evaluates to\
                 {evaluateFunction(eliteMember[0] + eliteMember[1] * 1j)}')
        if abs(evaluateFunction(eliteMember[0] + eliteMember[1] * 1j)) < MAX_ERROR:
            return eliteMember

        childrenPop = []
        for j, member in enumerate(population):
            a, b, c = getMembersBesides(population, member)
            newCh = member.copy()
            for i in range(SOLUTION_DIM):
                mutationProb = random.randint(0, 100) / 100
                if mutationProb < MUTATION_RATE:
                    newCh[i] = random.randint(LOWER_BOUND, UPPER_BOUND)

                crossProbability = random.randint(0, 100) / 100
                if crossProbability < CROSSOVER_PROBABILITY:
                    newCh[i] = a[i] + DIFFERENTIAL_FACTOR * (b[i] - c[i])

            if abs(evaluateFunction(member[0] + member[0] * 1j)) > \
                abs(evaluateFunction(newCh[0] + newCh[0] * 1j)):
                population[j] = newCh
    
    print('Could not find acceptable solution!')
    population = childrenPop.copy()
    return 0 + 0j