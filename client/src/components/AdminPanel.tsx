import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { Button, Form, Input, message, Spin } from 'antd';

interface MenuItem {
  label: string;
}

const AdminPanel: React.FC = () => {
  const [form] = Form.useForm();
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!isAuthenticated) {
      navigate('/auth-adm');
    }
  }, [isAuthenticated, navigate]);

  const onFinish = async (values: any) => {
    setLoading(true);
    console.log('Submitting form with values:', values);
    
    try {
      const response = await fetch('http://localhost:8000/api/draw-building/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Server response:', data);

        const newKey = data.id || Date.now().toString(); 


        const newItem: MenuItem = {
          label: data.message || 'New Item',
        };

              
        localStorage.setItem(newKey, JSON.stringify(newItem));

        message.success('Здание успешно нарисовано!');
        form.resetFields();
      } else {
        message.error('Не удалось нарисовать здание. Пожалуйста, попробуйте снова.');
        console.error('Response error:', await response.text());
      }
    } catch (error) {
      message.error('Произошла ошибка при рисовании здания.');
      console.error('Fetch error:', error);
    } finally {
      setLoading(false);
    }
  };
  

  return (
    <div style={{ position: 'relative', paddingBlock: 32 }}>
      <Spin spinning={loading} tip="Processing...">
        <Form
          form={form}
          onFinish={onFinish}
          scrollToFirstError={{ behavior: 'auto', block: 'end', focus: true }}
          labelCol={{ span: 6 }}
          wrapperCol={{ span: 14 }}
        >
          <Form.Item name="BuildingName" label="Building Name" rules={[{ required: true }]}>
            <Input />
          </Form.Item>

          <Form.Item name="address" label="Address" rules={[{ required: true }]}>
            <Input.TextArea rows={4} />
          </Form.Item>

          <Form.Item name="info" label="Info" rules={[{ required: true }]}>
            <Input.TextArea rows={6} />
          </Form.Item>

          <Form.Item name="color" label="Drawing color">
            <Input />
          </Form.Item>

          <Form.Item name="img" label="URL to image">
            <Input />
          </Form.Item>

          <Form.Item name="html" label="HTML for popup">
            <Input.TextArea rows={6} />
          </Form.Item>

          <Form.Item wrapperCol={{ offset: 6 }}>
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
            <Button danger onClick={() => form.resetFields()}>
              Reset
            </Button>
          </Form.Item>
        </Form>
      </Spin>
    </div>
  );
};

export default AdminPanel;
