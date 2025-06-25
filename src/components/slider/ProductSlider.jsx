import React from "react";
import Slider from "react-slick";
import sofa from '../../assets/sofa.jpeg'
import Bed from '../../assets/wooden-bed.jpg'
import chair from '../../assets/chair.jpg'
import styles from "./productSlider.module.css"; // You can style with CSS Modules

const products = [
  {
    id: 1,
    name: "Modern Sofa",
    price: "$499",
    discount: "20% OFF",
    image: sofa, // replace with your image path
  },
  {
    id: 2,
    name: "Wooden Bed",
    price: "$799",
    discount: null,
    image: Bed,
  },
  {
    id: 3,
    name: "Stylish Chair",
    price: "$129",
    discount: "10% OFF",
    image: chair,
  },
];

const ProductSlider = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    autoplay: true,
    autoplaySpeed: 3000,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
  };

  return (
    <div className={styles.sliderContainer}>
      <Slider {...settings}>
        {products.map((product) => (
          <div key={product.id} className={styles.slide}>
            <img src={product.image} alt={product.name} className={styles.image} />
            <div className={styles.details}>
              <h2>{product.name}</h2>
              <p className={styles.price}>{product.price}</p>
              {product.discount && <span className={styles.discount}>{product.discount}</span>}
              <button className={styles.button}>Shop Now</button>
            </div>
          </div>
        ))}
      </Slider>
    </div>
  );
};

export default ProductSlider;
