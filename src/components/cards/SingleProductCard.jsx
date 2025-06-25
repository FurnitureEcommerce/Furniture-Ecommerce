import React from 'react';
import styles from './productCard.module.css';
import { Link } from 'react-router-dom';

const SingleProductCard = ({ id, image, name, price, discount }) => {
  return (
    <div className={styles.card}>
      <img src={image} alt={name} className={styles.image} />
      <h3>{name}</h3>
      <p className={styles.price}>{price}</p>
      {discount && <span className={styles.discount}>{discount}</span>}
      
      <Link to={`/product/${id}`}>
        <button className={styles.button}>Shop Now</button>
      </Link>
    </div>
  );
};

export default SingleProductCard;
