import { HomeOutlined } from '@ant-design/icons';
import { Layout, Menu } from 'antd';
import React, { useState, useEffect } from 'react';

const { Header, Content, Sider } = Layout;

interface MenuItem {
  label: string;
}

const initialItems: MenuItem[] = [
  { label: 'Корпуса МИСИС' },
  { label: 'Общежития МИСИС' },
];

export const Map = () => {
  const [mapUrl, setMapUrl] = useState('/map.html');
  const [items, setItems] = useState<MenuItem[]>(initialItems); 

  useEffect(() => {
    const storedItems: MenuItem[] = [];

    for (let i = 1; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key) {
        const item = JSON.parse(localStorage.getItem(key) || '{}');
        if (item.label) {
          storedItems.push({ label: item.label });
        }
      }
    }

    setItems(prevItems => [...prevItems, ...storedItems]); 
    console.log("Retrieved items:", storedItems); 
  }, []);

  const handleMenuClick = (e: { key: string }) => {
    if (e.key === '0') {
      setMapUrl('/map-block-a.html');
    } else if (e.key === '1') {
      setMapUrl('/map-block-b.html'); 
    } else {
  
      const selectedItemIndex = parseInt(e.key) - initialItems.length; 
      if (selectedItemIndex >= 0 && selectedItemIndex < items.length) {
        const selectedItem = items[selectedItemIndex];
        const formattedLabel = selectedItem.label.replace(/\s+/g, '-').toLowerCase(); 
        setMapUrl(`/map-${formattedLabel}.html`); 
      }
    }
  };

  return (
    <Layout>
      <Sider width={'15%'}>
        <div className="demo-logo-vertical" />
        <Menu theme="light" defaultSelectedKeys={['0']} onClick={handleMenuClick}>
          {items.map((item, index) => (
            <Menu.Item key={(index + initialItems.length).toString()} icon={<HomeOutlined />}>
              {item.label}
            </Menu.Item>
          ))}
        </Menu>
      </Sider>
      <Layout>
        <Header />
        <Content style={{ margin: '24px 16px 0' }}>
          <div>
            <iframe
              src={mapUrl}
              title="Map"
              style={{
                width: '85%',
                height: '100vh',
                border: 'none',
                bottom: '0',
                right: '0',
                position: 'absolute',
              }}
            />
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};
