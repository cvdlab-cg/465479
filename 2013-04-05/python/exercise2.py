from pyplasm import *

SIMPLEX_GRID = COMP([INSR(PROD),AA(QUOTE)])

#PIANO TERRA
#definisco il pilastro circolare
circPill = CYLINDER([0.125,2.45])(36)
circPill_firstRow_0 = T([1])([0.125])(circPill)

#definisco il pilastro rettangolare
squarePill = PROD([CUBOID([0.25,0.25]),Q(2.45)])
squarePill = T([2])([-0.125])(squarePill)

#definisco blocchi di raccordo
circJunction = CYLINDER([0.125,0.25])(36)
circJunction = T([1])([0.125])(circPill)
squareJunction = PROD([CUBOID([0.25,0.25]),Q(0.25)])
squareJunction = T([2])([-0.125])(squareJunction)

#pilastri esterni, prima riga

traslation = T([1])([2.75])
external_pillars_0 = STRUCT(NN(5)([circPill_firstRow_0, traslation]))
external_junctions_0 = STRUCT(NN(5)([T([3])([-0.25])(circJunction), traslation]))
external_pillars_0 = STRUCT([external_pillars_0,external_junctions_0])

#pilastri interni, seconda riga
#prima i cilindrici
circPill_secondRow_0 = T([2])([5.25])(circPill_firstRow_0)
#poi i quadrati
squarePill_secondRow_0 = T([1])([2.75])(squarePill)
squarePill_secondRow_0 = T([2])([5.25])(squarePill_secondRow_0)
internal_pillars_0 = STRUCT([circPill_secondRow_0, STRUCT(NN(3)([squarePill_secondRow_0,traslation]))])

pillars0 = STRUCT([external_pillars_0,internal_pillars_0])


#PRIMO PIANO

squarePill_short = PROD([CUBOID([0.25,0.25]),Q(2.25)])
squarePill_short = T([2])([-0.125])(squarePill_short)
circPill_short = CYLINDER([0.125,2.25])(36)
circPill_short = T([1])([0.125])(circPill_short)

#pilastri esterni, prima riga, primo piano
squarePill_firstRow_1 = T([3])([2.70])(squarePill_short)
external_pillars_1 = STRUCT(NN(5)([squarePill_firstRow_1, traslation]))

#pilastri interni, seconda riga, primo piano
squarePill_secondRow_1 = T([2])([5.25])(squarePill_firstRow_1)
internal_pillars_1 = STRUCT(NN(3)([squarePill_secondRow_1, traslation]))
lastSquarePill_secondRow_1 = T([1])([11])(squarePill_secondRow_1)
#l'unico pilastro cilindrico
third_circPill_secondoRow_1 = T([1,2,3])([8.25,5.25,2.70])(circPill_short)
internal_pillars_1 = STRUCT([internal_pillars_1, third_circPill_secondoRow_1, lastSquarePill_secondRow_1])
#aggiungo i raccordi per col secondo piano
squareJunction_firstRow_1 = T([3])([5.20-0.25])(squareJunction)
external_Junction_firstRow_1 = STRUCT(NN(3)([squareJunction_firstRow_1, traslation]))
squareJunction_secondRow_1 = T([1,2,3])([2.75,5.25,5.20-0.25])(squareJunction)

pillars1 = STRUCT([internal_pillars_1,external_pillars_1,external_Junction_firstRow_1,squareJunction_secondRow_1])


#SECONDO PIANO
#partire da 5.2
#pilastri interni, prima riga, secondo piano
squarePill_firstRow_2 = T([3])([5.20])(squarePill_short)
external_pillars_2 = STRUCT(NN(3)([squarePill_firstRow_2, traslation]))
lastSquarePill_firstRow_2 = T([1])([11])(squarePill_firstRow_2)
external_pillars_2 = STRUCT([external_pillars_2, lastSquarePill_firstRow_2])

#pilastri esterni, seconda riga, secondo piano
squarePill_secondRow_2 = T([2,3])([5.25, 5.20])(squarePill_short)
internal_pillars_2 = STRUCT(NN(5)([squarePill_secondRow_2, traslation]))

#aggiungo i raccordi per col terzo piano
squareJunction_firstRow_2 = T([1,3])([5.5,7.70-0.25])(squareJunction)

pillars2 = STRUCT([external_pillars_2,internal_pillars_2,squareJunction_firstRow_2])


#TERZO PIANO
#definisco il pilastro rettangolare per l'ultimo piano (più basso)
squarePill_3 = PROD([CUBOID([0.25,0.25]),Q(2.30)])
squarePill_3 = T([2])([-0.125])(squarePill_3)
#codice di Giovanni Pace 465479
squarePill_small_3 = PROD([CUBOID([0.125,0.125]),Q(2.30)])
squarePill_small_3 = T([2])([-0.125])(squarePill_small_3)

#pilastri esterni, prima riga
squarePill1_firstRow_3 = T([1,3])([5.5,7.70])(squarePill_3)
squarePill2_firstRow_3 = T([1])([5.5])(squarePill1_firstRow_3)
external_pillars_3 = STRUCT([squarePill1_firstRow_3,squarePill2_firstRow_3])

#pilastri interni, seconda riga
#pilastri piccoli
squarePill1_small_secondRow_3 = T([2,3])([5.375,7.70])(squarePill_small_3)
squarePill2_small_secondRow_3 = T([1])([2.75])(squarePill1_small_secondRow_3)
squarePills_small_secondRow_3 = STRUCT([squarePill1_small_secondRow_3,squarePill2_small_secondRow_3])
#pilastri grande
squarePill_secondRow_3 = T([1,2,3])([5.5,5.25,7.70])(squarePill_3)
internal_pillars_3 = STRUCT(NN(3)([squarePill_secondRow_3, traslation]))
internal_pillars_3 = STRUCT([internal_pillars_3, squarePills_small_secondRow_3])

pillars3 = STRUCT([external_pillars_3,internal_pillars_3])

#EXERCISE 1
prato = SIMPLEX_GRID([[11.25],[7+0.125],[0.05]])
prato = COLOR([0,1,0])(prato)
prato = T([2,3])([-0.125,-0.25])(prato)

#Pavimento piano terra
#prima griglia, base per scalette esterne
little_stairs_0 = SIMPLEX_GRID([[1.50],[-5.125,1.875],[0.25]])

#cella centrale, piano terra
central_cell_0 = SIMPLEX_GRID([[-1.5,7],[-2,5],[0.25]])

#sx cell
sx_cell_0 = SIMPLEX_GRID([[-1.5,-7,1.3],[-2,-2.1,2.9],[0.25]])

#semicerchio destro
def annulus_sector (alpha, r, R):
    dom_u = INTERVALS(alpha)(36)
    dom_v = INTERVALS(R-r)(1)
    dom = PROD([dom_u,dom_v])
    def mapping(v):
        a = v[0]
        r = v[1]
        return [r*COS(a), r*SIN(a)]
    model = MAP(mapping)(dom)
    return model

semicircle_0 = annulus_sector(PI, 0, 1.25 + 0.20)
semicircle_0 = R([1,2])(-PI/2)(semicircle_0)
semicircle_0 = T([1,2])([1.5+7+1.3,2+2.5+1.25 -0.2])(semicircle_0)
semicircle_0 = PROD([semicircle_0,Q(0.25)])

#down micro cell
dw_cell_0 = SIMPLEX_GRID([[-1.50,1],[-1,1],[0.25]])

#semicerchio in basso
little_semicirle_0 = annulus_sector(PI,0,0.5)
little_semicirle_0 = R([1,2])(PI)(little_semicirle_0)
little_semicirle_0 = T([1,2])([1.5+0.5,1])(little_semicirle_0)

little_semicirle_0 = PROD([little_semicirle_0,Q(0.25)])

ground_floor = STRUCT([little_stairs_0,central_cell_0,sx_cell_0,semicircle_0,dw_cell_0, little_semicirle_0])
ground_floor = T([3])([-0.25])(ground_floor)

#Pavimento primo piano
floor_1_1 = SIMPLEX_GRID([[11.25],[5.50],[0.25]])
floor_2_1 = SIMPLEX_GRID([[4.95],[1.625],[0.25]])
floor_2_1 = T([1,2])([6.30,5.50])(floor_2_1)
floor_3_1 = SIMPLEX_GRID([[3.8],[1.875],[0.25]])
floor_3_1 = T([1,2])([-1.5,5.25])(floor_3_1)
floor_4_1 = SIMPLEX_GRID([[6.30],[0.25],[0.25]])
floor_4_1 = T([2])([6.875])(floor_4_1)

floor_1 = STRUCT([floor_1_1,floor_2_1,floor_3_1,floor_4_1])
floor_1 = T([2,3])([-0.125,2.45])(floor_1)

#Pavimento secondo piano
floor_1_2 = SIMPLEX_GRID([[5.75],[7],[0.25]])
floor_1_2 = T([1])([5.5])(floor_1_2)
floor_2_2 = SIMPLEX_GRID([[0.5],[1.5],[0.25]])
floor_2_2 = T([1,2])([5,5.50])(floor_2_2)
verts = POLYLINE([[5.5,0],[5.5,5.5],[5,5.5],[5.5,0]])
floor_3_2 = SOLIDIFY(verts)
floor_3_2 = PROD([floor_3_2,Q(0.25)])
floor_4_2 = SIMPLEX_GRID([[5],[0.25],[0.25]])
floor_4_2 = T([1,2])([0.25,7-0.25])(floor_4_2)
floor_5_2 = SIMPLEX_GRID([[0.25],[1.75],[0.25]])
floor_5_2 = T([2])([5.25])(floor_5_2)

floor_2 = STRUCT([floor_1_2,floor_2_2,floor_3_2,floor_4_2,floor_5_2])
floor_2 = T([2,3])([-0.125,4.95])(floor_2)


#Pavimento terzo piano
#prima griglia a sinistra del terzo piano
sx_cell_3 = SIMPLEX_GRID([[5.75],[7],[0.25]])

#prima griglia a destra del terzo piano
dx_cell_3 = SIMPLEX_GRID([[-5.75,3.125],[5.525],[0.25]])

#seconda griglia a destra del terzo piano
dx_second_cell_3 = SIMPLEX_GRID([[-5.75,-3,2.5],[5.4,1.6],[0.25]])

floor3 = STRUCT([sx_cell_3,dx_cell_3,dx_second_cell_3])
floor3 = T([2,3])([-0.125,7.45])(floor3)


#QURATO PIANO: Tetto
sx_cell_4 = SIMPLEX_GRID([[5.625],[0.25,-5,1.75],[0.25]])

#prima griglia a destra del terzo piano
dx_cell_4 = SIMPLEX_GRID([[-5.625,5.625],[7],[0.25]])
#contorno
crosswalk = SIMPLEX_GRID([[0.25],[0.25,5],[0.25]])

floor4 = STRUCT([sx_cell_4,dx_cell_4,crosswalk])
floor4 = T([2,3])([-0.125,9.75])(floor4)


floors = STRUCT([floor_1,floor_2,floor3,ground_floor,floor4])


building = STRUCT([pillars0, pillars1, pillars2, pillars3, floors, prato])
VIEW(building) 
