const path = require('path');

module.exports = {
    entry: '/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
    mode: 'development',
    // Avoid using eval() by setting devtool to 'cheap-module-source-map' or 'source-map'
    devtool: 'cheap-module-source-map',
};