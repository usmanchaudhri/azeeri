const merge = function (objects) {
    console.log(objects)

    var out = {}
    for(var i=0; i<objects.length; i++) {
        for(var p in objects[i]) {
            out[p] = obects[i][p]
        }
    }
    return out;
}

merge([1,2,3])


