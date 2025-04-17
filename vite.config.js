import { defineConfig } from 'vite'
import path from 'path'

export default defineConfig({
  root: './frontend/src', // your actual source code lives here
  build: {
    outDir: '../../backend/static/frontend', // where Django will find it
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, 'src/main.js'),
        style: path.resolve(__dirname, 'src/style.css'),
      },
      output: {
        entryFileNames: '[name].js',
        assetFileNames: '[name].css',
      }
    },
  },
})
