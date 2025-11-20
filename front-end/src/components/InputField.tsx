import React from "react";

interface InputFieldProps {
  label: string;
  name: string;
  value: string | number;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  type?: string;
}

export default function InputField({
  label,
  name,
  value,
  onChange,
  type = "number",
}: InputFieldProps) {
  return (
    <div className="flex flex-col gap-1">
      <label className="text-sm font-semibold">{label}</label>
      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        className="p-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500"
      />
    </div>
  );
}
