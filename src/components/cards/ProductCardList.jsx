// ProductCardList.jsx
import React from 'react';
import SingleProductCard from './SingleProductCard';
import styles from './productCard.module.css';
import products from '../product/productsData'; 


const ProductCardList = () => {
  return (
    <div className={styles.gridContainer}>
      {products.map(product => (
        <SingleProductCard
          key={product.id}
          id={product.id}
          image={product.image}
          name={product.name}
          price={product.price}
          discount={product.discount}
        />
      ))}
    </div>
  );
};

export default ProductCardList;
