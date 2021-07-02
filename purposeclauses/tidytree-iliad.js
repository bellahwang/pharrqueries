var margin = {top: 10, right: 15, bottom: 20, left: 30},
    width = 800 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var data = {
    "wID": "0",
    "id": "ROOT",
    "children": [
        {
            "wID": "10",
            "form": ".",
            "lemma": ".",
            "postag": "u--------",
            "head": "0",
            "relation": "AuxK",
            "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
            "id": "._10"
        },
        {
            "wID": "11",
            "form": "[0]",
            "head": "0",
            "relation": "COORD",
            "id": "[0]_11",
            "children": [
                {
                    "wID": "2",
                    "form": "ἴθι",
                    "lemma": "εἶμι",
                    "postag": "v2spma---",
                    "head": "11",
                    "relation": "PRED_CO",
                    "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                    "id": "ἴθι_2",
                    "children": [
                        {
                            "wID": "1",
                            "form": "ἀλλ'",
                            "lemma": "ἀλλά",
                            "postag": "d--------",
                            "head": "2",
                            "relation": "AuxY",
                            "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                            "id": "ἀλλ'_1"
                        }
                    ]
                },
                {
                    "wID": "5",
                    "form": "ἐρέθιζε",
                    "lemma": "ἐρεθίζω",
                    "postag": "v2spma---",
                    "head": "11",
                    "relation": "PRED_CO",
                    "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                    "id": "ἐρέθιζε_5",
                    "children": [
                        {
                            "wID": "3",
                            "form": "μή",
                            "lemma": "μή",
                            "postag": "d--------",
                            "head": "5",
                            "relation": "AuxZ",
                            "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                            "id": "μή_3"
                        },
                        {
                            "wID": "4",
                            "form": "μ'",
                            "lemma": "ἐγώ",
                            "postag": "p-s---ma-",
                            "head": "5",
                            "relation": "OBJ",
                            "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                            "id": "μ'_4"
                        }
                    ]
                },
                {
                    "wID": "7",
                    "form": "ὥς",
                    "lemma": "ὡς",
                    "postag": "c--------",
                    "head": "11",
                    "relation": "AuxC",
                    "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                    "id": "ὥς_7",
                    "children": [
                        {
                            "wID": "9",
                            "form": "νέηαι",
                            "lemma": "νέομαι",
                            "postag": "v2spse---",
                            "head": "7",
                            "relation": "ADV",
                            "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                            "id": "νέηαι_9",
                            "children": [
                                {
                                    "wID": "6",
                                    "form": "σαώτερος",
                                    "lemma": "σῶς",
                                    "postag": "a-s---mnc",
                                    "head": "9",
                                    "relation": "AtvV",
                                    "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                                    "id": "σαώτερος_6"
                                },
                                {
                                    "wID": "8",
                                    "form": "κε",
                                    "lemma": "ἄν",
                                    "postag": "g--------",
                                    "head": "9",
                                    "relation": "AuxZ",
                                    "cite": "urn:cts:greekLit:tlg0012.tlg001:1.32",
                                    "id": "κε_8"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

var root = d3.hierarchy(data);
    root.dx = 10;
    root.dy = width / (root.height + 1);

var tree = d3.tree().nodeSize([root.dx, root.dy])(root);

let x0 = Infinity;
let x1 = -x0;
root.each(d => {
    if (d.x > x1) x1 = d.x;
    if (d.x < x0) x0 = d.x;
});

var svg = d3.select("#tidytree")
    .append("svg")
        .attr("width", width)
        .attr("height", height)

var g = svg.append("g")
    .attr("font-family", "sans-serif")
    .attr("font-size", 10)
    .attr("transform", "translate(90,90)");  // bit of margin on the left = 40

var link = g.append("g")
    .attr("fill", "none")
    .attr("stroke", "#555")
    .attr("stroke-opacity", 0.4)
    .attr("stroke-width", 1.5)
    .selectAll("path")
    .data(root.links())
    .join("path")
        .attr("d", d3.linkHorizontal()
            .x(d => d.y)
            .y(d => d.x))
        .classed("link", true)

/* link.append("text")
    .attr("font-family", "sans-serif")
    .attr("font-size", 10)
    .attr("transform", function(d) {
        return "translate(" +
            ((d.source.y + d.target.y)/2) + "," + 
            ((d.source.x + d.target.x)/2) + ")";
    })   
    .attr("dy", ".35em")
    .text(function(d) {
        console.log(d.target.data.relation);
        return d.target.data.relation;
    }); */

/* link.append("text")
        .attr("dy", "0.31em")
        .attr("x", d => d.source.x + (d.target.x - d.source.x)/2)
        .attr("text-anchor", d => "middle")
        .text(d => d.target.data.form)
    .clone(true).lower()
        .attr("stroke", "white") */
        
var tooltip = d3.select("body").append("div")	
    .style("opacity", 0)
    .attr("class", "tooltip")

var mouseover = function(event, d) {
    tooltip.transition()
        .duration(200)
        .style("opacity", .9)

    tooltip.html("form: " + d.data.form + "\n" + 
        "lemma: " + d.data.lemma + "\n" + 
        "postag: " + d.data.postag + "\n" +
        "cite: " + d.data.cite)
        .style("left", (event.pageX) + "px")
        .style("top", (event.pageY - 28) + "px")
}

var mouseleave = function(d) {
    tooltip.transition()
        .duration(500)
        .style("opacity", 0)
}

var node =  g.append("g")
    .attr("stroke-linejoin", "round")
    .attr("stroke-width", 3)
    .selectAll("g")
        .data(root.descendants())
        .join("g")
            .attr("transform", d => `translate(${d.y},${d.x})`)

node.append("circle")
    .attr("fill", d => d.children ? "#EEA7A5" : "#92a8d1")
    .attr("r", 4)
    .on("mouseover", mouseover)
    .on("mouseleave", mouseleave)
    
node.append("text")
        .attr("dy", "0.31em")
        .attr("x", d => d.children ? -6 : 6)
        .attr("text-anchor", d => d.children ? "end" : "start")
        .text(d => d.data.form)
        .attr("font-size", 12)
    .clone(true).lower()
        .attr("stroke", "white")

link.enter().append("text")
    .attr("transform", function(d) {
        return "translate(" +
            ((d.source.y + d.target.y)/2) + "," + 
            ((d.source.x + d.target.x)/2) + ")";
    })
    .attr("text-anchor", "middle")
    .text(d => d.target.data.relation)