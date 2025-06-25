import React from 'react';
import ProductSlider from '../components/slider/ProductSlider';
import ProductCardList from '../components/cards/ProductCardList';

const HomePage = () => {
  return (
    <div>
      <ProductSlider />
      <ProductCardList />
    </div>
  );
};

export default HomePage;