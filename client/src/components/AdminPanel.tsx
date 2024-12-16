import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import { Button, Form, Input, message, Spin } from 'antd';

const AdminPanel: React.FC<{ onBuildingSaved: (name: string) => void }> = ({ onBuildingSaved }) => {
  const [form] = Form.useForm();
  const navigate = useNavigate();
  const { isAuthenticated } = useAuth();
  const [loading, setLoading] = useState(false);

  if (!isAuthenticated) {
    navigate('/auth-adm');
    return null;
  }

  const onFinish = async (values: any) => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/draw-building/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });

      if (response.ok) {
        const buildingName = values.BuildingName; 
        onBuildingSaved(buildingName); 
        message.success('Building drawn successfully!');
        form.resetFields();
      } else {
        message.error('Failed to draw building. Please try again.');
      }
    } catch (error) {
      message.error('An error occurred while drawing the building.');
      console.error(error);
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
