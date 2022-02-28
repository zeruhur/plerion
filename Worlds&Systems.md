---
nav_exclude: true 
---

# Worlds & Systems

## Space Geography 

The enormous expanses that access to oddspace has made traversable have generated the need to map the vastness of the Five Galaxies. 
Normal space is subdivided into 10pc-sided cubes, called sub-sectors. 

Below is the conventional scale in which the Charted Space is subdivided:
- **Sub-sector**: A region of 10pc<sup>3</sup> space in which there are several star systems.
- **Sector**: A region of 100pc<sup>3</sup> space or 1000 sub-sectors. 
- **Cluster**: Aggregation of 2 or more sectors, usually defined by political entities.
- **Quadrant**: A quarter of a galaxy, containing several territories each.

To this geography is added the topography of the Wormhole Access Network (WAN). Numerous natural and man-made wormholes are maintained to connect distant sectors and shorten travel times. Usually travel between wormholes is instantaneous and subject to a fee. A pair of wormholes is in exclusive communication, often natural wormholes are single way, while artificial wormholes are always double way, unless disabled on purpose.

## Astrography

The space is usually mapped at the local sub-sector level.  To represent a three-dimensional space, it is possible to "squash" the representation into two dimensions, representing the distances between nearest stars as edges of a graph.

```graphviz
digraph G {
    edge[arrowhead=none];
    node[shape=circle, fixedsize=1, width=0.1, label=""];
    
    a[color=yellow, style=filled];
    b[color=orange, style=filled];  
    c[color=red, style=filled];
    b[color=blue, style=filled];  
    
    a -> b 
    a -> c
    b -> c
    a -> d
    c -> d
    b -> e
    c -> e
    a -> f
    d -> f
}
```
| Spectral Type | Color        | Temperature Range   | Prevalence of among Main Sequence Stars | Examples              |
|               |              |                     |                                         |                       |
| O             | Blue-violet  | >30,000 K           | 0.00003%                                | Stars of Orion's Belt |
| B             | Blue-white   | 10,000 K - 30,000 K | 0.13%                                   | Rigel                 |
| A             | White        | 7,500 K - 10,000 K  | 0.6%                                    | Sirius                |
| F             | Yellow-white | 6,000 K - 7,500 K   | 3%                                      | Polaris               |
| G             | Yellow       | 5,000 K - 6,000 K   | 7.6%                                    | Sun                   |
| K             | Orange       | 3,500 K - 5000 K    | 12.1%                                   | Arcturus              |
| M             | Red-orange   | <3,500 K            | 76.5%                                   | Proxima Centauri      |