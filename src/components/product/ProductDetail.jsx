import React, { useState, useRef } from 'react';
import { useParams } from 'react-router-dom';
import products from './productsData';
import styles from './productDetail.module.css';

const ProductDetail = () => {
  const { id } = useParams();
  const product = products.find(p => p.id === parseInt(id));
  const imgRef = useRef(null);

  const [lensVisible, setLensVisible] = useState(false);
  const [lensPosition, setLensPosition] = useState({ x: 0, y: 0 });
  const [backgroundPosition, setBackgroundPosition] = useState('0% 0%');

  const handleMouseMove = (e) => {
    const bounds = imgRef.current.getBoundingClientRect();
    const x = e.clientX - bounds.left;
    const y = e.clientY - bounds.top;

    // Keep the lens inside the image
    const limitedX = Math.max(0, Math.min(x, bounds.width));
    const limitedY = Math.max(0, Math.min(y, bounds.height));

    const percentX = (limitedX / bounds.width) * 100;
    const percentY = (limitedY / bounds.height) * 100;

    setLensPosition({ x: limitedX, y: limitedY });
    setBackgroundPosition(`${percentX}% ${percentY}%`);
  };

  if (!product) return <p>Product not found</p>;

  return (
    <div className={styles.detailContainer}>
      <div
        className={styles.imageWrapper}
        onMouseEnter={() => setLensVisible(true)}
        onMouseLeave={() => setLensVisible(false)}
        onMouseMove={handleMouseMove}
      >
        <img
          ref={imgRef}
          src={product.image}
          alt={product.name}
          className={styles.mainImage}
        />

        {lensVisible && (
          <div
            className={styles.magnifier}
            style={{
              left: `${lensPosition.x - 75}px`,
              top: `${lensPosition.y - 75}px`,
              backgroundImage: `url(${product.image})`,
              backgroundPosition: backgroundPosition,
            }}
          />
        )}
      </div>

      {/* Zoom Preview on the right */}
      {lensVisible && (
        <div
          className={styles.zoomPreview}
          style={{
            backgroundImage: `url(${product.image})`,
            backgroundPosition: backgroundPosition,
          }}
        ></div>
      )}

      {/* Product Details */}
      <div className={styles.details}>
        <h2>{product.name}</h2>
        <p>{product.price}</p>
        {product.discount && <p className={styles.discount}>{product.discount}</p>}
      </div>
    </div>
  );
};

export default ProductDetail;
