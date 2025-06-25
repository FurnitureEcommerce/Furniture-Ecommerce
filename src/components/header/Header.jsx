import React from 'react'
import styles from './header.module.css'
import searchicon from '../../assets/search1.png'
import cart from '../../assets/cart.png'

const Header = () => {
  return (
    <>
    <header className={styles.head}>
        <div className={styles.headleft}>
            <span className={styles.log}>Login</span>
            <span className={styles.log}><img className={styles.search} src={searchicon} alt="search" /></span>
            <span className={styles.log}><img src={cart} alt="cart" /></span>
        </div>
        <nav className={styles.headright}>
            <span className={styles.tag}>New</span>

            
            <div className={styles.dropdownContainer}>
                <span className={styles.tag}>Collection</span>
                <div className={styles.dropdownMenu}>
                <ul>
                    <li>Jess Designs</li>
                    <li>Verandas Collection</li>
                    <li>Miller Lounge Series</li>
                    <li>Advi Series</li>
                </ul>
                </div>
            </div>
            {/* Dropdown ends */}
            <div className={styles.dropdownContainer}>
                <span className={styles.tag}>Furniture</span>
                <div className={styles.dropdownMenu}>
                <ul>
                    <li>Entry Way</li>
                    <li>Living</li>
                    <li>Dining</li>
                    <li>Bedroom</li>
                </ul>
                </div>
            </div>
            <div className={styles.dropdownContainer}>
                <span className={styles.tag}>Outdoor</span>
                <div className={styles.dropdownMenu}>
                <ul>
                    <li>Outdoor lounge</li>
                    <li>Outdoor dining</li>
                    <li>Outdoor decor</li>
                    
                </ul>
                </div>
            </div>
            
            <div className={styles.dropdownContainer}>
                    <span className={styles.tag}>Decor</span>
                        <div className={styles.dropdownMenu}>
                            <ul>
                                <li>Mirrors</li>
                                <li>Storages</li>
                                <li>Home Fragrance</li>
                                <li>Art</li>
                            </ul>
                            </div>
            </div>
            
        </nav>

        
        
        
    </header>
    </>
    
  )
}

export default Header