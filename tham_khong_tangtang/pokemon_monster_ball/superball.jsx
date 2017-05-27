function si(d,k,n){ //ฟังก์ชันสำหรับกำหนดสี
    var si = new RGBColor();
    si.red = d;
    si.green = k;
    si.blue = n;
    return si;}

documents.add(DocumentColorSpace.CMYK,512,512);

chaklang = app.activeDocument.pathItems.rectangle(512,0,512,512);
chaklang.filled = 1;
chaklang.fillColor = si(13,106,255);
chaklang.stroked = 0;

layer = app.activeDocument.layers.add();
thaep = layer.pathItems.add();
thaep.filled = 1;
thaep.fillColor = si(237,15,84);
thaep.stroked = 0;

var chut = [[160,476],[200,476],[200,36],[160,36]];
chut.push(chut[0])
thaep.setEntirePath(chut);
thaep.pathPoints[1].rightDirection = [chut[1][0]-70,chut[1][1]-50]
thaep.pathPoints[2].leftDirection = [chut[2][0]-70,chut[2][1]+50]
thaep.pathPoints[3].rightDirection = [chut[3][0]-120,chut[3][1]+50]
thaep.pathPoints[4].leftDirection = [chut[4][0]-120,chut[4][1]-50]

thaep = layer.pathItems.add();
thaep.filled = 1;
thaep.fillColor = si(237,15,84);
thaep.stroked = 0;

var chut = [[352,476],[312,476],[312,36],[352,36]];
chut.push(chut[0])
thaep.setEntirePath(chut);
thaep.pathPoints[1].rightDirection = [chut[1][0]+70,chut[1][1]-50]
thaep.pathPoints[2].leftDirection = [chut[2][0]+70,chut[2][1]+50]
thaep.pathPoints[3].rightDirection = [chut[3][0]+120,chut[3][1]+50]
thaep.pathPoints[4].leftDirection = [chut[4][0]+120,chut[4][1]-50]
