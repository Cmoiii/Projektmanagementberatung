import sets
import classes


def checkAttribute(answer: classes.Answer, method : classes.ProjectMethod, attribute: classes.MethodAttribute, set, idealMethods, alternativeMethods):
    if method in alternativeMethods:
        if set.index(answer.value) < set.index(attribute.min) or set.index(answer.value) > set.index(attribute.max):
            if method in idealMethods:
                idealMethods.remove(method)
            alternativeMethods.remove(method)
        elif set.index(answer.value) < set.index(attribute.ideal_min) or set.index(answer.value) > set.index(attribute.ideal_max):
            if method in idealMethods:
                idealMethods.remove(method)
            if answer.ideal == True and method in alternativeMethods:
                alternativeMethods.remove(method)
                return
            else: method.notIdeal.append(answer)   

def checkAttributeInt(answer: classes.Answer, method : classes.ProjectMethod, attribute: classes.MethodAttribute, idealMethods, alternativeMethods):
    if method in alternativeMethods:
        if answer.value < attribute.min or answer.value > attribute.max:
            if method in idealMethods:
                idealMethods.remove(method)
            alternativeMethods.remove(method)
        elif answer.value < attribute.ideal_min or answer.value > attribute.ideal_max:
            if method in idealMethods:
                idealMethods.remove(method)
            if answer.ideal == True and method in alternativeMethods:
                alternativeMethods.remove(method)
                return
            else: method.notIdeal.append(answer)

def check(answers):
    idealMethods = sets.methods.copy()
    alternativeMethods = sets.methods.copy()
    for answer in answers:
        for method in sets.methods:
            match answer.attribute.name:
                case "teams":
                    checkAttributeInt(answer, method, method.teams, idealMethods, alternativeMethods)
                case "teamsize":
                    checkAttributeInt(answer, method, method.teamsize, idealMethods, alternativeMethods)
                case "client":
                    checkAttribute(answer, method, method.client, answer.attribute.set, idealMethods, alternativeMethods)
                case "dependency":
                    checkAttribute(answer, method, method.dependency, answer.attribute.set, idealMethods, alternativeMethods)
                case "deadline":
                    checkAttribute(answer, method, method.deadline, answer.attribute.set, idealMethods, alternativeMethods)
                case "anforderung":
                    checkAttribute(answer, method, method.anforderung, answer.attribute.set, idealMethods, alternativeMethods)
    return idealMethods, alternativeMethods