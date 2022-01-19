

def quality_gate_111(features, labels):
    try:
        if (len(features)==117) & (len(labels)==117) & (features[0].shape==(1024, 1024,3))& (type(labels[0])==str):
            return "Quality gate passed :)"
        return "Quality gate failed :("
    except:
        return "Quality gate failed :("
    
def quality_gate_112(features, labels):
    try:
        if (len(features)==117) & (len(labels)==117) & (features[0].shape==(64,)):
            return "Quality gate passed :)"
        return "Quality gate failed :("
    except:
        return "Quality gate failed :("
    

def quality_gate_13(features, labels):
    try:
        percentage = X_train.shape[0]/(X_test.shape[0]+X_train.shape[0])
        if (percentage>0.6) & (percentage<0.8):
            return "Quality gate passed :)"
        return "Quality gate failed :("
    except:
        return "Quality gate failed :("
    
 
def quality_gate_141(y_train, y_test):
    try:
        percentage = y_train.shape[0]/(y_test.shape[0]+y_train.shape[0])
        if (percentage>0.75) & (percentage<0.85) & (y_test[0].shape==(3,)):
            return "Quality gate passed :)"
        return "Quality gate failed :("
    except:
        return "Quality gate failed :("