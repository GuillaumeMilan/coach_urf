class D3Require:
    def _repr_html_(self):
        return """
            <script>
            require.config({
                paths: {
                    d3: 'https://d3js.org/d3.v5.min'
                }
            });
            require(['d3'], function(d3) { window['d3']= d3})
            </script>
        """
