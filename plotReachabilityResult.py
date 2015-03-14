import matplotlib.pyplot as plt
import numpy as np

def autolabel(rects,ax):
    # attach some text labels
    i = 0
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%d'%int(height),
                ha='center', va='bottom')
        i = i + 1

def plotReachabilityResult(result,savefig=False):
	n_groups = len(result["reachable"])
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.4
	rects1 = plt.bar(index, result["reachable"], bar_width, alpha=opacity, color="b", label="Reachable")
	rects2 = plt.bar(index+bar_width, result["i-reachable"], bar_width, alpha=opacity, color="r", label="i-Reachable")

	plt.xlabel("Independencies")
	plt.ylabel("Number of Checks")
	if result.has_key("inaugurals"):
		plt.title("Reachable vs i-Reachable in " + result["title"] + " - I:" + result["inaugurals"].__str__())
	else:
		plt.title("Reachable vs i-Reachable in " + result["title"])
	plt.xticks(index + bar_width, result["tests"])
	plt.legend()

	plt.ylim([0,max(result["reachable"] + result["i-reachable"]) + 0.3*max(result["reachable"] + result["i-reachable"])])

	autolabel(rects1,ax)
	autolabel(rects2,ax)

	if savefig:
		plt.savefig("figures/" + result["title"] + ".png")
	else:
		plt.show()