function organizeData(data) {
    const root = d3.hierarchy(data);
    const width = 600
    root.dx = 10;
    root.dy = width / (root.height + 1);
    return d3.tree().nodeSize([root.dx, root.dy])(root);
    console.log("completed organization of data")
}

function drawChart(container, data) {
    const width = 600

    const root = organizeData(data);

    let x0 = Infinity;
    let x1 = -x0;
    root.each(d => {
    if (d.x > x1) x1 = d.x;
    if (d.x < x0) x0 = d.x;
    });

    const svg = d3
        .select(container)
        .append('svg')
        .attr('width', width)
        .attr('height', x1 - x0 + root.dx * 2);

    const g = svg.append("g")
        .attr("font-family", "sans-serif")
        .attr("font-size", 10)
        .attr("transform", `translate(${root.dy / 3},${root.dx - x0})`);

    const link = g.append("g")
        .attr("fill", "none")
        .attr("stroke", "#555")
        .attr("stroke-opacity", 0.4)
        .attr("stroke-width", 1.5)
        .selectAll("path")
        .data(root.links())
        .join("path")
            .attr("d", d3.linkHorizontal()
                .x(d => d.y)
                .y(d => d.x));

    const node = g.append("g")
        .attr("stroke-linejoin", "round")
        .attr("stroke-width", 3)
        .selectAll("g")
        .data(root.descendants())
        .join("g")
        .attr("transform", d => `translate(${d.y},${d.x})`)

    node.append("circle")
        .attr("fill", d => d.children ? "#EEA7A5" : "#92a8d1")
        .attr("r", 2.5)

    node.append("text")
        .attr("dy", "0.31em")
        .attr("x", d => d.children ? -6 : 6)
        .attr("text-anchor", d => d.children ? "end" : "start")
        .text(d => d.data.form)
        .clone(true).lower()
        .attr("stroke", "white");
}