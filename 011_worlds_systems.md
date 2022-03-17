# Worlds & Systems
The enormous expanses that access to oddspace has made traversable have generated the need to map the vastness of the Five Galaxies. This chapter will provide the fundamentals for managing the geography of space and generating star systems.

## Space Geography 
Normal space is subdivided into 10pc-sided cubes, called sub-sectors. 

Below is the conventional scale in which the Charted Space is subdivided:
- **Sub-sector**: A region of 10pc<sup>3</sup> space in which there are several star systems.
- **Sector**: A region of 100pc<sup>3</sup> space or 1000 sub-sectors. 
- **Cluster**: Aggregation of 2 or more sectors, usually defined by political entities.
- **Quadrant**: A quarter of a galaxy, containing several sectors each.

<img src="_assets/graphviz/sector_dia.png" width="600px">

To this geography is added the topography of the Wormhole Access Network (WAN). Numerous natural and man-made wormholes are maintained to connect distant sectors and shorten travel times. Usually travel between wormholes is instantaneous and subject to a fee. A pair of wormholes is in exclusive communication, often natural wormholes are single way, while artificial wormholes are always double way, unless disabled on purpose.

## Astrography

Space is usually mapped at the local sub-sector level.  To represent a three-dimensional space, it is possible to "press" the representation into two dimensions, representing the distances between nearest stars as edges of a graph.

<img src="_assets/graphviz/subsector_dia.svg" width="600px">

To determine the configuration of a sub-sector:
1. Roll 2d20 to determine the number of stars of the region.
2. For each star roll 1d6, then add the values ​​of two nearby stars to calculate the distance in light-years between them.
3. Draw the resulting graph, noting the distances.

Optionally, it is possible to drop a number of colored d6s (representing the spectral class of the stars) on a sheet of paper, thus drawing the edges of the graph between them and marking the sum value of each pair.

## Stellar Systems

The generation of features for a star system can be randomly determined using this procedure. Roll on the relevant tables where necessary.  
When prompted 1d3, roll 1d6, divide by two and round down.

1. Roll for number of stars in the system.
2. Roll for spectral type and color.
3. Roll 1d6+4 to determine the number of planets.
4. Roll 1d6 to determine the number of habitats.
   - If one of them is a ringworld/Dyson sphere, there are no other planets in the system.
5. Roll for planet type. 
   - Roll 1d3 to determine how many worlds are in the habitable zone.
6. Roll for planet features.
7. Roll to determine moons:
   -. For gas/ice giant planets, roll 1d20 to termine the number of moons. Roll for determine type and features of each.
   -. For terrestrial planets, roll 1d3. Then roll for type and features.
   -. For dwarf planets, roll 1-6. If result is 6 they have one satellite.
   -. Habitats and asteroid belts have no moons.
8. Roll on Population table to determine each moon inhabitants. They always capped to 10mln.

Giant/dwarf planets and asteroids are naturally uninhabitable, but they are settled using domed and underground facilities (see Colonies below).

### Number of Stars per System

|   1-3  |  4-18  |    19   |        20        |
|:------:|:------:|:-------:|:----------------:|
| Single | Binary | Trinary | Multiple (1d6+1) |


### Star Spectral Type

|    1-15    |  16-17 |   18   |   19  |      20      |
|:----------:|:------:|:------:|:-----:|:------------:|
|      M     |    K   |   F/G  |   A   |    Special   |
| Red-Orange | Orange | Yellow | White | (roll below) |


|     1-14    |     15    |     16     |    17-18   |     19-20    |
|:-----------:|:---------:|:----------:|:----------:|:------------:|
|      T      |     M     |      B     |      -     |       -      |
| Brown Dwarf | Red Giant | Blue Giant | Black Hole | Neutron Star |

### Star Dimension (don't roll for special)

|  1-17 |   18   |     19     |     20     |
|:-----:|:------:|:----------:|:----------:|
| Dwarf |  Giant | Supergiant | Hypergiant |

### Planets and Habitats

#### Planet Type

|    1-5    |    6-10   |    11-17    | 18-19 |       20      |
|:---------:|:---------:|:-----------:|:-----:|:-------------:|
| Gas Giant | Ice Giant | Terrestrial | Dwarf | Asteroid Belt |

#### Habitat Type

|       |                    |       |               |
|:-----:| ------------------ |:-----:| ------------- |
|  1-4  | O'Neil Cylinder    | 15-16 | Bishop Ring   |
|  5-6  | McKendree Cylinder | 17-18 | Banks Orbital |
|  7-9  | Stanford Torus     |   19  | Dyson Sphere  |
| 10-14 | Bernal Sphere      |   20  | Ringworld     |

#### Terrestrial Planet Features

|     |                |     |             |     |             |     |              |
| --- | -------------- | --- | ----------- | --- | ----------- | --- | ------------ |
| 1   | Barren         | 6   | Savanna     | 11  | Forest      | 16  | Ecumenopolis |
| 2   | Frozen         | 7   | Arctic      | 12  | Archipelago | 17  | Garden World |
| 3   | Arid           | 8   | Steppe      | 13  | Waterworld  | 18  | Hellworld    |
| 4   | Desert         | 9   | Continental | 14  | Tropical    | 19  | Tainted      |
| 5   | Tidally Locked | 10  | Relic       | 15  | Hothouse    | 20  | Ruined       |

#### Moon Size and Type

|             1-10            |    11-14   |   15-18  | 19-20 |
|:---------------------------:|:----------:|:--------:|:-----:|
| Planetary-mass (roll below) | Small Rock | Big Rock |  Ring |


|  1-15  |  16-17 |    18    |    19    |     20    |
|:------:|:------:|:--------:|:--------:|:---------:|
| Barren | Frozen | Vulcanic | Hothouse | Habitable |

### Planet/Habitat Features

#### Government

|      |              |       |             |
|:----:| ------------ |:-----:| ----------- |
|  1-2 | Corporate    | 11-12 | Anarchy     |
|  3-4 | Democracy    | 13-14 | Technocracy |
|  5-6 | Oligarchy    | 15-16 | Autocracy   |
|  7-8 | Dictatorship | 17-18 | Bureaucracy |
| 9-10 | Feudal       | 19-20 | Theocracy   |

#### Economy

|       |              |       |                  |
|:-----:| ------------ |:-----:| ---------------- |
|  1-6  | Agricultural | 15-16 | Mining           |
|  7-11 | Industrial   | 17-19 | Political Center |
| 12-14 | Finance      |   20  | Religious Center |

#### GDP Level

|      |         |       |      |
|:----:| ------- |:-----:| ---- |
|  1-4 | Poor    | 13-16 | Good |
|  5-8 | Low     | 17-19 | High |
| 9-12 | Average |   20  | Rich |

#### Technological Level

|     |             |       |                  |
|:---:| ----------- |:-----:| ---------------- |
|  1  | Stone Age   |  6-7  | Atomic Age       |
|  2  | Metal Age   |  8-9  | Information Age  |
|  3  | Clock Age   | 10-11 | Space Age        |
|  4  | Steam Age   | 12-13 | Stellar Age      |
|  5  | Machine Age | 14-20 | Interstellar Age |

#### Population

Roll 1d20: on 19-20 the planet is uninhabited, else roll on the following table.

|      |        |       |         |
|:----:| ------ |:-----:| ------- |
|  1-2 | 10+    | 11-12 | 1mln+   |
|  3-4 | 100+   | 13-14 | 10mln+  |
|  5-6 | 1,000+ | 15-16 | 100mln+ |
|  7-8 | 10k+   | 17-18 | 1bln+   |
| 9-10 | 100k+  | 19-20 | 10bln+* |

### Space Stations & Bases
Space stations are quite common in any star system and cannot be determined with a specific algorithm. Usually there can 1d20 stations per planet.  They are usually installed in orbit, on the surface of inhospitable planets and at strategic points such as Langrange Points. To inspire the referee who needs it, here are some examples.

|       1-4       |       5-8      |     9-12     |        13-16       |         17-20        |
|:---------------:|:--------------:|:------------:|:------------------:|:--------------------:|
| Wheeled Station | Zero-G Station | Void Citadel | Domed Installation | Underground Facility |


|      |                        |       |                   |
|:----:| ---------------------- |:-----:| ----------------- |
|  1-2 | Science Lab            | 11-12 | Chemicals Factory |
|  3-4 | Astronomic Observatory | 13-14 | Mining Station    |
|  5-6 | Military Base          | 15-16 | Solar Power Plant |
|  7-8 | Weapon Factory         | 17-18 | Farm              |
| 9-10 | Electronics Factory    | 19-20 | Idroponics        |

### Colonies
Inhospitable planets, Gas and Ice Giants, and asteroids can still be inhabited thanks to artificial structures generically called colonies.

|    1-4   |             5-8             |       9-12       |    13-16   |       17-20      |
|:--------:|:---------------------------:|:----------------:|:----------:|:----------------:|
| Arcology | Modular Ground Installation | Floating Citadel | Domed City | Underground Base |

