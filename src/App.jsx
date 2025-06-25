import Header from "./components/header/header"
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";
import Footer from "./components/footer/Footer";
import ProductDetail from "./components/product/ProductDetail";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from "./Page/HomePage";




function App() {
  

  return (
    <>
    <Router>
      <Header/>
        
        <Routes>
          <Route path='/' element={<HomePage/>}></Route>
          <Route path="/product/:id" element={<ProductDetail/>} />

        </Routes>
      
      <Footer/>

    </Router>
      
      
    </>
  )
}

export default App


/*

*/