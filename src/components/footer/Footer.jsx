import React from 'react';
import styles from './footer.module.css';

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.section}>
        <h3>Contact</h3>
        <p>Email: support@furnihub.com</p>
        <p>Phone: +91 98765 43210</p>
      </div>

      <div className={styles.section}>
        <h3>Address</h3>
        <p>FurniHub Pvt. Ltd.</p>
        <p>123, Furniture Lane, Kochi, Kerala</p>
      </div>

      <div className={styles.section}>
        <h3>Follow Us</h3>
        <p><a href="#">Instagram</a></p>
        <p><a href="#">Facebook</a></p>
        <p><a href="#">Twitter</a></p>
      </div>

      <div className={styles.section}>
        <h3>Policy</h3>
        <p><a href="#">Privacy Policy</a></p>
        <p><a href="#">Return Policy</a></p>
        <p><a href="#">Terms & Conditions</a></p>
      </div>
    </footer>
  );
};

export default Footer;
