# Create Dictionary Here

# Needed Output

"HTML Progress Is 90%"
"CSS Progress Is 80%"
"Python Progress Is 30%"
"AI Progress Is 20%"
compe={
    "one":{
        "langue":"html",
        "Progress":"90%"
    },
     "two":{
        "langue":"css",
        "Progress":"80%"
    },
     "three":{
        "langue":"pyhon",
        "Progress": "30%"
    }
}
print(f"{compe['one']["langue"]} Progress {compe['one']["Progress"]}")
print(f"{compe['two']["langue"]} Progress {compe['two']["Progress"]}")
print(f"{compe['three']["langue"]} Progress {compe['three']["Progress"]}")
compe.update({"four":{"langue":"ai","Progress":"20%"}})
print(f"{compe['four']["langue"]} Progress {compe['four']["Progress"]}")
